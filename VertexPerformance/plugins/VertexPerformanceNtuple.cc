#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Common/interface/TriggerNames.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandomEngine.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "RecoVertex/VertexPrimitives/interface/VertexException.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

#include "RecoVertex/PrimaryVertexProducer/interface/GapClusterizerInZ.h"
#include "RecoVertex/PrimaryVertexProducer/interface/DAClusterizerInZ.h"
#include "RecoVertex/PrimaryVertexProducer/interface/DAClusterizerInZ_vect.h"
#include "RecoVertex/AdaptiveVertexFit/interface/AdaptiveVertexFitter.h"

#include "SimDataFormats/TrackingAnalysis/interface/TrackingVertexContainer.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"

#include "CLHEP/Random/RandFlat.h"

#include "TTree.h"
#include "TH1F.h"

namespace {
  class VertexPrinter {
  public:
    VertexPrinter(const TransientVertex& v): vertex(v) {}

    void print(std::ostream& os) const {
      if(vertex.isValid()) {
        os << "valid " << vertex.position();
      }
      else {
        os << "invalid";
      }
    }

  private:
    const TransientVertex& vertex;
  };

  std::ostream& operator<<(std::ostream& os, const VertexPrinter& vp) {
    vp.print(os);
    return os;
  }

  bool matchVertex(const reco::Vertex& recoVertex, const TrackingVertex& simVertex) {
    constexpr double absZ_ = 0.1;
    constexpr double sigmaZ_ = 3;

    const double zdiff = std::abs(recoVertex.z() - simVertex.position().z());
    return zdiff < absZ_ && zdiff / recoVertex.zError() < sigmaZ_;
  }

  std::vector<const TrackingVertex *> matchVertices(const reco::Vertex& recoVertex, const std::vector<const TrackingVertex *>& trackingVertices) {
    std::vector<const TrackingVertex *> ret;

    for(const TrackingVertex *simVertexP: trackingVertices) {
      if(matchVertex(recoVertex, *simVertexP)) {
        ret.push_back(simVertexP);
      }
    }
    return ret;
  }
}

class VertexPerformanceNtuple: public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit VertexPerformanceNtuple(const edm::ParameterSet&);
  ~VertexPerformanceNtuple();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) override;

  void book();
  void reset();

  void doResolution(const std::vector<reco::TransientTrack>& tracks, CLHEP::HepRandomEngine& engine, const reco::BeamSpot& beamspot, const reco::Vertex& pv);
  void doEfficiency(const std::vector<reco::TransientTrack>& tracks, CLHEP::HepRandomEngine& engine, const reco::BeamSpot& beamspot, const reco::Vertex& pv);

  edm::EDGetTokenT<reco::TrackCollection> trackSrc_;
  edm::EDGetTokenT<reco::VertexCollection> vertexSrc_;
  edm::EDGetTokenT<reco::BeamSpot> beamspotSrc_;
  edm::EDGetTokenT<edm::TriggerResults> triggerSrc_;

  const bool minimal_;
  const bool useTrackingParticles_;
  edm::EDGetTokenT<TrackingVertexCollection> trackingVertexSrc_;

  std::unique_ptr<TrackClusterizerInZ> clusterizer_;
  AdaptiveVertexFitter fitter_;

  TTree *tree;

  edm::RunNumber_t b_run;
  edm::LuminosityBlockNumber_t b_lumi;
  edm::EventNumber_t b_event;

  int b_nsimvertices;
  int b_nvertices;
  int b_nvertices_good;

  struct TriggerPath {
    TriggerPath(const std::string& n): name(n), value(false) {}

    void book(TTree *tree, const std::string& prefix) {
      tree->Branch((prefix+name).c_str(), &value);
    }
    void reset() { value = false; }

    const std::string name;
    bool value;
  };

  std::vector<TriggerPath> b_triggers;

  struct Beamspot {
    void book(TTree *tree, const std::string& prefix) {
      tree->Branch((prefix+"_x").c_str(), &x);
      tree->Branch((prefix+"_y").c_str(), &y);
      tree->Branch((prefix+"_z").c_str(), &z);
    }
    void set(const reco::BeamSpot& bs) {
      x = bs.x0();
      y = bs.y0();
      z = bs.z0();
    }
    void reset() {
      x = 0; y = 0; z = 0;
    }
    double x;
    double y;
    double z;
  };


  struct VerticesLight {
    void book(TTree *tree, const std::string& prefix, bool useTrackingParticles=false) {
      tree->Branch((prefix+"_valid").c_str(), &valid);
      tree->Branch((prefix+"_fake").c_str(), &fake);
      tree->Branch((prefix+"_z").c_str(), &z);
      tree->Branch((prefix+"_ntracks").c_str(), &ntracks);

      if(useTrackingParticles) {
        tree->Branch((prefix+"_matchedSimVertices").c_str(), &matchedSimVertices);
        tree->Branch((prefix+"_matchedToSimPV").c_str(), &matchedToSimPV);
      }
    }

    void append(const reco::Vertex& vertex, const std::vector<const TrackingVertex *>& trackingVertices, const TrackingVertex *simPV) {
      fake.push_back(vertex.isFake());
      valid.push_back(vertex.isValid());
      z.push_back(vertex.z());
      ntracks.push_back(vertex.tracksSize());

      if(!trackingVertices.empty()) {
        matchedSimVertices.push_back(matchVertices(vertex, trackingVertices).size());
        matchedToSimPV.push_back(matchVertex(vertex, *simPV));
      }
    }

    void reset() {
      z.clear();
      ntracks.clear();
      fake.clear(); valid.clear();

      matchedSimVertices.clear(); matchedToSimPV.clear();
    }

    std::vector<double> z;
    std::vector<int> ntracks;
    std::vector<bool> fake;
    std::vector<bool> valid;

    std::vector<int> matchedSimVertices;
    std::vector<bool> matchedToSimPV;
  };


  struct Vertices {
    Vertices() {}

    void book(TTree *tree, const std::string& prefix, bool useTrackingParticles=false) {
      tree->Branch((prefix+"_valid").c_str(), &valid);
      tree->Branch((prefix+"_fake").c_str(), &fake);
      tree->Branch((prefix+"_x").c_str(), &x);
      tree->Branch((prefix+"_y").c_str(), &y);
      tree->Branch((prefix+"_z").c_str(), &z);
      tree->Branch((prefix+"_rho").c_str(), &rho);
      tree->Branch((prefix+"_x_error").c_str(), &x_error);
      tree->Branch((prefix+"_y_error").c_str(), &y_error);
      tree->Branch((prefix+"_z_error").c_str(), &z_error);
      tree->Branch((prefix+"_ndof").c_str(), &ndof);
      tree->Branch((prefix+"_chi2").c_str(), &chi2);
      tree->Branch((prefix+"_ntracks").c_str(), &ntracks);
      tree->Branch((prefix+"_sumpt").c_str(), &sumpt); 
      tree->Branch((prefix+"_sumpt2").c_str(), &sumpt2);

      if(useTrackingParticles) {
        tree->Branch((prefix+"_matchedSimVertices").c_str(), &matchedSimVertices);
        tree->Branch((prefix+"_matchedToSimPV").c_str(), &matchedToSimPV);
      }
    }

    void append(const reco::Vertex& vertex, const std::vector<const TrackingVertex *>& trackingVertices, const TrackingVertex *simPV) {
      appendInt(vertex);

      double sumpt_=0, sumpt2_=0;
      for(auto iTrack = vertex.tracks_begin(); iTrack != vertex.tracks_end(); ++iTrack) {
        const auto pt = (*iTrack)->pt();
        sumpt_ += pt;
        sumpt2_ += pt*pt;
      }
      sumpt.push_back(sumpt_);
      sumpt2.push_back(sumpt2_);

      if(!trackingVertices.empty()) {
        matchedSimVertices.push_back(matchVertices(vertex, trackingVertices).size());
        matchedToSimPV.push_back(matchVertex(vertex, *simPV));
      }
    }

    void append(const TransientVertex& vertex) {
      appendInt(vertex);

      double sumpt_=0, sumpt2_=0;
      for(const auto& track: vertex.originalTracks()) {
        const auto pt = track.track().pt();
        sumpt_ += pt;
        sumpt2_ += pt*pt;
      }
      sumpt.push_back(sumpt_);
      sumpt2.push_back(sumpt2_);
    }

    void appendInt(const reco::Vertex& vertex) {
      fake.push_back(vertex.isFake());
      valid.push_back(vertex.isValid());
      x.push_back(vertex.x());
      y.push_back(vertex.y());
      z.push_back(vertex.z());
      rho.push_back(vertex.position().rho());
      x_error.push_back(vertex.xError());
      y_error.push_back(vertex.yError());
      z_error.push_back(vertex.zError());
      ntracks.push_back(vertex.tracksSize());
      chi2.push_back(vertex.chi2());
      ndof.push_back(vertex.ndof());
    }

    void reset() {
      x.clear(); y.clear(); z.clear(); rho.clear();
      x_error.clear(); y_error.clear(); z_error.clear();
      ndof.clear(); chi2.clear(); ntracks.clear();
      sumpt.clear(); sumpt2.clear();
      fake.clear(); valid.clear();

      matchedSimVertices.clear(); matchedToSimPV.clear();
    }

    std::vector<double> x;
    std::vector<double> y;
    std::vector<double> z;
    std::vector<double> rho;
    std::vector<double> x_error;
    std::vector<double> y_error;
    std::vector<double> z_error;
    std::vector<double> ndof;
    std::vector<double> chi2;
    std::vector<int> ntracks;
    std::vector<double> sumpt;
    std::vector<double> sumpt2;
    std::vector<bool> fake;
    std::vector<bool> valid;

    std::vector<int> matchedSimVertices;
    std::vector<bool> matchedToSimPV;
  };

  struct SimVertices {
    SimVertices() {}

    void book(TTree *tree, const std::string& prefix) {
      tree->Branch((prefix+"_x").c_str(), &x);
      tree->Branch((prefix+"_y").c_str(), &y);
      tree->Branch((prefix+"_z").c_str(), &z);
      tree->Branch((prefix+"_ntracks").c_str(), &ntracks);
      tree->Branch((prefix+"_sumpt").c_str(), &sumpt); 
      tree->Branch((prefix+"_sumpt2").c_str(), &sumpt2);
    }

    void append(const TrackingVertex& vertex) {
      x.push_back(vertex.position().x());
      y.push_back(vertex.position().y());
      z.push_back(vertex.position().z());
      ntracks.push_back(vertex.nDaughterTracks());

      double sumpt_=0, sumpt2_=0;
      for(auto iTrack=vertex.daughterTracks_begin(); iTrack != vertex.daughterTracks_end(); ++iTrack) {
        const auto pt = (*iTrack)->pt();
        sumpt_ += pt;
        sumpt2_ += pt*pt;
      }
      sumpt.push_back(sumpt_);
      sumpt2.push_back(sumpt2_);
    }

    void reset() {
      x.clear(); y.clear(); z.clear();
      ntracks.clear();
      sumpt.clear(); sumpt2.clear();
    }

    std::vector<double> x;
    std::vector<double> y;
    std::vector<double> z;
    std::vector<int> ntracks;
    std::vector<double> sumpt;
    std::vector<double> sumpt2;
  };

  Beamspot b_bs;
  Vertices b_pv;
  VerticesLight b_puv;

  SimVertices b_simpv;

  Vertices b_res_vertex1;
  int b_res_vertex1_tracks_size;
  Vertices b_res_vertex2;
  int b_res_vertex2_tracks_size;

  Vertices b_eff_vertexTag;
  int b_eff_vertexTag_tracks_size;
  Vertices b_eff_vertexProbe;
  int b_eff_vertexProbe_tracks_size;

  struct TrackPlots {
    explicit TrackPlots(const std::string& pref): prefix(pref) {}

    void book(TFileService& fs) {
      trackpt = fs.make<TH1F>((prefix+"_track_pt").c_str(), "Track pT", 1000, 0, 100);
      tracketa = fs.make<TH1F>((prefix+"_track_eta").c_str(), "Track #eta", 120, -3.0, 3.0);
      trackphi = fs.make<TH1F>((prefix+"_track_phi").c_str(), "Track #phi", 128, -3.2, 3.2);
      trackdxy = fs.make<TH1F>((prefix+"_track_dxy").c_str(), "Track dxy", 800, -0.4, 0.4);
      trackdz = fs.make<TH1F>((prefix+"_track_dz").c_str(), "Track dz", 300, -15, 15);
      trackdxy_bs = fs.make<TH1F>((prefix+"_track_dxy_bs").c_str(), "Track dxy wrt. beamspot", 800, -0.4, 0.4);
      trackdz_bs = fs.make<TH1F>((prefix+"_track_dz_bs").c_str(), "Track dz wrt. beamspot", 300, -15, 15);
      trackdxy_pv = fs.make<TH1F>((prefix+"_track_dxy_pv").c_str(), "Track dxy wrt. PV", 800, -0.4, 0.4);
      trackdz_pv = fs.make<TH1F>((prefix+"_track_dz_pv").c_str(), "Track dz wrt. PV", 1000, -1, 1);
    }

    void fill(const std::vector<reco::TransientTrack>& tracks, const reco::BeamSpot& beamspot, const reco::Vertex& pv) {
      for(const reco::TransientTrack& track: tracks) {
        fill(track.track(), beamspot, pv);
      }
    }

    void fill(const reco::Track& track, const reco::BeamSpot& beamspot, const reco::Vertex& pv) {
      trackpt->Fill(track.pt());
      tracketa->Fill(track.eta());
      trackphi->Fill(track.phi());
      trackdxy->Fill(track.dxy());
      trackdz->Fill(track.dz());
      trackdxy_bs->Fill(track.dxy(beamspot.position()));
      trackdz_bs->Fill(track.dz(beamspot.position()));
      trackdxy_pv->Fill(track.dxy(pv.position()));
      trackdz_pv->Fill(track.dz(pv.position()));
    }

    std::string prefix;
    TH1 *trackpt;
    TH1 *tracketa;
    TH1 *trackphi;
    TH1 *trackdxy;
    TH1 *trackdz;
    TH1 *trackdxy_bs;
    TH1 *trackdz_bs;
    TH1 *trackdxy_pv;
    TH1 *trackdz_pv;
  };

  TrackPlots h_res_tracks_pv;
  TrackPlots h_res_tracks_set1;
  TrackPlots h_res_tracks_set2;

  TrackPlots h_eff_tracks_pv;
  TrackPlots h_eff_tracks_setTag;
  TrackPlots h_eff_tracks_setProbe;
};

VertexPerformanceNtuple::VertexPerformanceNtuple(const edm::ParameterSet& iConfig):
  trackSrc_(consumes<reco::TrackCollection>(iConfig.getUntrackedParameter<edm::InputTag>("trackSrc"))),
  vertexSrc_(consumes<reco::VertexCollection>(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc"))),
  beamspotSrc_(consumes<reco::BeamSpot>(iConfig.getUntrackedParameter<edm::InputTag>("beamspotSrc"))),
  triggerSrc_(consumes<edm::TriggerResults>(iConfig.getUntrackedParameter<edm::InputTag>("triggerResultsSrc"))),
  minimal_(iConfig.getUntrackedParameter<bool>("minimal")),
  useTrackingParticles_(iConfig.getUntrackedParameter<bool>("useTrackingParticles")),
  h_res_tracks_pv("res_pv"),
  h_res_tracks_set1("res_set1"),
  h_res_tracks_set2("res_set2"),
  h_eff_tracks_pv("eff_pv"),
  h_eff_tracks_setTag("eff_setTag"),
  h_eff_tracks_setProbe("eff_setProbe")
{
  for(const std::string& name: iConfig.getUntrackedParameter<std::vector<std::string>>("triggers")) {
    b_triggers.emplace_back(name);
  }

  if(useTrackingParticles_) {
    trackingVertexSrc_ = consumes<TrackingVertexCollection>(iConfig.getUntrackedParameter<edm::InputTag>("trackingVertexSrc"));
  }

  // From PrimaryVertexProducer
  // select and configure the track clusterizer
  edm::ParameterSet pset = iConfig.getUntrackedParameter<edm::ParameterSet>("TkClusParameters");
  std::string clusteringAlgorithm=pset.getParameter<std::string>("algorithm");
  if (clusteringAlgorithm=="gap"){
    clusterizer_.reset(new GapClusterizerInZ(pset.getParameter<edm::ParameterSet>("TkGapClusParameters")));
  }else if(clusteringAlgorithm=="DA"){
    clusterizer_.reset(new DAClusterizerInZ(pset.getParameter<edm::ParameterSet>("TkDAClusParameters")));
  }
  // provide the vectorized version of the clusterizer, if supported by the build
#ifdef __GXX_EXPERIMENTAL_CXX0X__
  else if(clusteringAlgorithm == "DA_vect") {
    clusterizer_.reset(new DAClusterizerInZ_vect(pset.getParameter<edm::ParameterSet>("TkDAClusParameters")));
  }
#endif
  else{
    throw VertexException("PrimaryVertexProducerAlgorithm: unknown clustering algorithm: " + clusteringAlgorithm);  
  }

  usesResource("TFileService");
  edm::Service<TFileService> fs;

  tree = fs->make<TTree>("tree", "Tree");
  book();

  h_res_tracks_pv.book(*fs);
  h_res_tracks_set1.book(*fs);
  h_res_tracks_set2.book(*fs);
  if(!minimal_) {
    h_eff_tracks_pv.book(*fs);
    h_eff_tracks_setTag.book(*fs);
    h_eff_tracks_setProbe.book(*fs);
  }
}

VertexPerformanceNtuple::~VertexPerformanceNtuple() {}

void VertexPerformanceNtuple::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.addUntracked<edm::InputTag>("trackSrc", edm::InputTag("generalTracks"));
  desc.addUntracked<edm::InputTag>("vertexSrc", edm::InputTag("offlinePrimaryVertices"));
  desc.addUntracked<edm::InputTag>("beamspotSrc", edm::InputTag("offlineBeamSpot"));
  desc.addUntracked<edm::InputTag>("triggerResultsSrc", edm::InputTag("TriggerResults", "", "HLT"));
  desc.addUntracked<std::vector<std::string>>("triggers", std::vector<std::string>());

  desc.addUntracked<bool>("minimal", false);
  desc.addUntracked<bool>("useTrackingParticles", false);
  desc.addUntracked<edm::InputTag>("trackingVertexSrc", edm::InputTag("mix", "MergedTrackTruth"));

  // copy contents from process.unsortedOfflinePrimaryVertices.TkClusParameters to this PSet
  edm::ParameterSetDescription descNested;
  //descNested.addUntracked<std::string>("foo", "");
  descNested.setAllowAnything();

  desc.addUntracked<edm::ParameterSetDescription>("TkClusParameters", descNested);

  descriptions.add("vertexPerformanceNtuple", desc);
}

void VertexPerformanceNtuple::book() {
  tree->Branch("run", &b_run);
  tree->Branch("lumi", &b_lumi);
  tree->Branch("event", &b_event);

  for(auto& trigger: b_triggers) {
    trigger.book(tree, "trig_");
  }

  b_bs.book(tree, "bs");

  if(!minimal_) {
    tree->Branch("nsimvertices", &b_nsimvertices);
  }
  tree->Branch("nvertices", &b_nvertices);
  tree->Branch("nvertices_good", &b_nvertices_good);

  b_pv.book(tree, "pv", useTrackingParticles_);
  if(!minimal_) {
    b_puv.book(tree, "puv", useTrackingParticles_);
  }
  if(useTrackingParticles_) {
    b_simpv.book(tree, "simpv");
  }

  b_res_vertex1.book(tree, "res_vertex1");
  tree->Branch("res_vertex1_tracks_size", &b_res_vertex1_tracks_size);

  b_res_vertex2.book(tree, "res_vertex2");
  tree->Branch("res_vertex2_tracks_size", &b_res_vertex2_tracks_size);

  if(!minimal_) {
    b_eff_vertexTag.book(tree, "eff_vertexTag");
    tree->Branch("eff_vertexTag_tracks_size", &b_eff_vertexTag_tracks_size);

    b_eff_vertexProbe.book(tree, "eff_vertexProbe");
    tree->Branch("eff_vertexProbe_tracks_size", &b_eff_vertexProbe_tracks_size);
  }

  reset();
}

void VertexPerformanceNtuple::reset() {
  b_run=0; b_lumi=0; b_event=0;
  for(auto& trigger: b_triggers) {
    trigger.reset();
  }

  b_bs.reset();

  b_nsimvertices=0;
  b_nvertices=0; b_nvertices_good=0;
  b_pv.reset();
  b_puv.reset();
  b_simpv.reset();

  b_res_vertex1.reset();
  b_res_vertex1_tracks_size = 0;

  b_res_vertex2.reset();
  b_res_vertex2_tracks_size = 0;

  b_eff_vertexTag.reset();
  b_eff_vertexTag_tracks_size = 0;

  b_eff_vertexProbe.reset();
  b_eff_vertexProbe_tracks_size = 0;
}

void VertexPerformanceNtuple::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  edm::Handle<edm::TriggerResults> htrigger;
  iEvent.getByToken(triggerSrc_, htrigger);
  const edm::TriggerResults& trigger = *htrigger;

  const edm::TriggerNames& triggerNames = iEvent.triggerNames(trigger);
  for(size_t i=0; i<triggerNames.size(); ++i) {
    for(auto& path: b_triggers) {
      if(triggerNames.triggerName(i) == path.name)
        path.value = trigger.accept(i);
    }
  }

  edm::Handle<reco::TrackCollection> htracks;
  iEvent.getByToken(trackSrc_, htracks);
  const reco::TrackCollection& tracks = *htracks;

  edm::Handle<reco::VertexCollection> hvertices;
  iEvent.getByToken(vertexSrc_, hvertices);
  const reco::VertexCollection& vertices = *hvertices;

  edm::Handle<reco::BeamSpot> hbeamspot;
  iEvent.getByToken(beamspotSrc_, hbeamspot);
  const reco::BeamSpot& beamspot = *hbeamspot;

  const TrackingVertex *simPV = nullptr;
  std::vector<const TrackingVertex *> trackingVertices;
  if(useTrackingParticles_) {
    edm::Handle<TrackingVertexCollection> htv;
    iEvent.getByToken(trackingVertexSrc_, htv);
    const TrackingVertexCollection& tvs = *htv;
    int current_event = -1;
    for(const TrackingVertex& v: tvs) {
      // Associate only to primary vertices of the in-time pileup
      // events (BX=0, first vertex in each of the events)
      if(v.eventId().bunchCrossing() != 0) continue;
      if(v.eventId().event() != current_event) {
        current_event = v.eventId().event();
        trackingVertices.push_back(&v);
        if(v.eventId().event() == 0)
          simPV = &v;
      }
    }
  }

  edm::ESHandle<TransientTrackBuilder> ttBuilderHandle;
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", ttBuilderHandle);
  const TransientTrackBuilder& ttBuilder = *ttBuilderHandle;

  edm::Service<edm::RandomNumberGenerator> rng;
  CLHEP::HepRandomEngine& engine = rng->getEngine(iEvent.streamID());

  b_run = iEvent.id().run();
  b_lumi = iEvent.id().luminosityBlock();
  b_event = iEvent.id().event();

  b_nsimvertices = trackingVertices.size();
  b_nvertices = vertices.size();
  b_nvertices_good = 0;
  for(const auto& v: vertices) {
    if(v.ndof() >= 4)
      ++b_nvertices_good;
  }

  b_bs.set(beamspot);

  if(simPV) {
    b_simpv.append(*simPV);
  }

  if(!vertices.empty()) {
    // For now, do it only for "the PV"
    const reco::Vertex& thePV = vertices[0];
    b_pv.append(thePV, trackingVertices, simPV);

    for(size_t i=1; i<vertices.size(); ++i) {
      b_puv.append(vertices[i], trackingVertices, simPV);
    }


    if(thePV.tracksSize() >= 4) {
      edm::LogInfo("VertexPerformanceNtuple") << "Primary vertex at " << thePV.position() << " with " << thePV.tracksSize() << " tracks";

      std::vector<const reco::Track *> sortedTracks;
      sortedTracks.reserve(thePV.tracksSize());
      std::transform(thePV.tracks_begin(), thePV.tracks_end(), std::back_inserter(sortedTracks), [](const reco::TrackBaseRef& ref) {
          return &(*ref);
        });
      std::sort(sortedTracks.begin(), sortedTracks.end(), [](const reco::Track *a, const reco::Track *b) {
          return a->pt() > b->pt();
        });

      std::vector<reco::TransientTrack> ttracks;
      ttracks.reserve(sortedTracks.size());
      std::transform(sortedTracks.begin(), sortedTracks.end(), std::back_inserter(ttracks), [&](const reco::Track *track) {
          auto tt =  ttBuilder.build(track);
          tt.setBeamSpot(beamspot);
          return tt;
        });

      doResolution(ttracks, engine, beamspot, thePV);
      if(!minimal_ && thePV.tracksSize() >= 6) {
        doEfficiency(ttracks, engine, beamspot, thePV);
      }
    }
  }
  tree->Fill();
  reset();
}

void VertexPerformanceNtuple::doResolution(const std::vector<reco::TransientTrack>& ttracks, CLHEP::HepRandomEngine& engine, const reco::BeamSpot& beamspot, const reco::Vertex& pv) {
  const size_t end = ttracks.size()%2 == 0 ? ttracks.size() : ttracks.size()-1;

  std::vector<reco::TransientTrack> set1, set2;
  set1.reserve(end/2); set2.reserve(end/2);

  for(size_t i=0; i<end; i += 2) {
    // engine->flat() returns double in ]0, 1[ , this rescales it to ]0, 2[ and truncates to 0 or 1
    const size_t set1_i = CLHEP::RandFlat::shootInt(&engine, 0, 2);
    const size_t set2_i = 1-set1_i;

    set1.push_back(ttracks[i+set1_i]);
    set2.push_back(ttracks[i+set2_i]);
  }

  h_res_tracks_pv.fill(ttracks, beamspot, pv);
  h_res_tracks_set1.fill(set1, beamspot, pv);
  h_res_tracks_set2.fill(set2, beamspot, pv);

  b_res_vertex1_tracks_size = set1.size();
  b_res_vertex2_tracks_size = set2.size();

  // For resolution we only fit
  TransientVertex vertex1 = fitter_.vertex(set1);
  TransientVertex vertex2 = fitter_.vertex(set2);

  edm::LogVerbatim("VertexPerformanceNtuple") << "Set1: " << set1.size() << " tracks, vertex " << VertexPrinter(vertex1);
  edm::LogVerbatim("VertexPerformanceNtuple") << "Set2: " << set2.size() << " tracks, vertex " << VertexPrinter(vertex2);

  b_res_vertex1.append(vertex1);
  b_res_vertex2.append(vertex2);
}

void VertexPerformanceNtuple::doEfficiency(const std::vector<reco::TransientTrack>& ttracks, CLHEP::HepRandomEngine& engine, const reco::BeamSpot& beamspot, const reco::Vertex& pv) {
  // 2/3 for tag, 1/3 for probe
  std::vector<reco::TransientTrack> setTag, setProbe;
  setTag.reserve(2*ttracks.size()/3+1); setProbe.reserve(ttracks.size()/3+1);

  const size_t end = ttracks.size() - ttracks.size()%3;
  for(size_t i=0; i<end; i+= 3) {
    const size_t probe_i = CLHEP::RandFlat::shootInt(&engine, 0, 3);
    setProbe.push_back(ttracks[i+probe_i]);

    for(size_t j=0; j<3; ++j) {
      if(j == probe_i) continue;
      setTag.push_back(ttracks[i+probe_i]);
    }
  }
  if(ttracks.size()%3 == 1) {
    const int probeOrTag = CLHEP::RandFlat::shootInt(&engine, 0, 3);
    if(probeOrTag == 0) { // 1/3 probability for probe
      setProbe.push_back(ttracks[end]);
    }
    else { // 2/3 for tag
      setTag.push_back(ttracks[end]);
    }
  }
  else if(ttracks.size()%3 == 2) {
    const size_t probe_i = CLHEP::RandFlat::shootInt(&engine, 0, 3);
    if(probe_i < 2) { // 2/3 one track to probe, other to tag
      const size_t tag_i = 1-probe_i;
      setProbe.push_back(ttracks[end+probe_i]);
      setTag.push_back(ttracks[end+tag_i]);
    }
    else { // 1/3 both to tag
      setTag.push_back(ttracks[end]);
      setTag.push_back(ttracks[end+1]);
    }
  }

  h_eff_tracks_pv.fill(ttracks, beamspot, pv);
  h_eff_tracks_setTag.fill(setTag, beamspot, pv);
  h_eff_tracks_setProbe.fill(setProbe, beamspot, pv);

  b_eff_vertexTag_tracks_size = setTag.size();
  b_eff_vertexProbe_tracks_size = setProbe.size();

  // Here we also cluster in addition to fit
  std::vector< std::vector<reco::TransientTrack> > && clustersTag =  clusterizer_->clusterize(setTag);
  std::vector< std::vector<reco::TransientTrack> > && clustersProbe =  clusterizer_->clusterize(setProbe);
  edm::LogVerbatim("VertexPerformanceNtuple") << "SetTag: " << setTag.size() << " tracks, " << clustersTag.size() << " clusters";
  for(const auto& cluster: clustersTag) {
    if(cluster.size() < 2) {
      edm::LogVerbatim("VertexPerformanceNtuple") << "  cluster has " << cluster.size() << " tracks, ignoring";
      continue;
    }
    TransientVertex vertex = fitter_.vertex(cluster);
    b_eff_vertexTag.append(vertex);
    
    edm::LogVerbatim("VertexPerformanceNtuple") << " vertex " << VertexPrinter(vertex);
  }

  edm::LogVerbatim("VertexPerformanceNtuple") << "SetProbe: " << setProbe.size() << " tracks, " << clustersProbe.size() << " clusters";
  for(const auto& cluster: clustersProbe) {
    if(cluster.size() < 2) {
      edm::LogVerbatim("VertexPerformanceNtuple") << "  cluster has " << cluster.size() << " tracks, ignoring";
      continue;
    }
    TransientVertex vertex = fitter_.vertex(cluster);
    b_eff_vertexProbe.append(vertex);
    edm::LogVerbatim("VertexPerformanceNtuple") << " vertex " << VertexPrinter(vertex);
  }

}

DEFINE_FWK_MODULE(VertexPerformanceNtuple);

