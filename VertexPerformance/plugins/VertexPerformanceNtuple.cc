#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/EDGetToken.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandomEngine.h"

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

#include "CLHEP/Random/RandFlat.h"

#include "TTree.h"

class VertexPerformanceNtuple: public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit VertexPerformanceNtuple(const edm::ParameterSet&);
  ~VertexPerformanceNtuple();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) override;

  void book();
  void reset();

  void doResolution(const std::vector<reco::TransientTrack>& tracks, CLHEP::HepRandomEngine& engine);
  void doEfficiency(const std::vector<reco::TransientTrack>& tracks, CLHEP::HepRandomEngine& engine);

  edm::EDGetTokenT<reco::VertexCollection> vertexSrc_;
  edm::EDGetTokenT<reco::BeamSpot> beamspotSrc_;

  std::unique_ptr<TrackClusterizerInZ> clusterizer_;
  AdaptiveVertexFitter fitter_;

  TTree *tree;

  edm::RunNumber_t b_run;
  edm::LuminosityBlockNumber_t b_lumi;
  edm::EventNumber_t b_event;

  int b_nvertices;
  int b_nvertices_good;

  /*
  struct Vertex {
    Vertex() { reset(); }

    void book(TTree *tree, const std::string& prefix) {
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
      tree->Branch((prefix+"_valid").c_str(), &valid);
      tree->Branch((prefix+"_fake").c_str(), &fake);
    }

    void set(const reco::Vertex& vertex) {
      fake = vertex.isFake();
      if(vertex.isValid()) {
        valid = true;
        x = vertex.x();
        y = vertex.y();
        z = vertex.z();
        rho = vertex.position().rho();
        x_error = vertex.xError();
        y_error = vertex.yError();
        z_error = vertex.zError();
        ntracks = vertex.tracksSize();
        chi2 = vertex.chi2();
        ndof = vertex.ndof();
      }
    }

    void reset() {
      x=0.; y=0.; z=0; rho=0.;
      x_error=0.; y_error=0.; z_error=0.;
      ndof=0; chi2=0; ntracks=0;
      fake=false; valid=false;
    }

    double x;
    double y;
    double z;
    double rho;
    double x_error;
    double y_error;
    double z_error;
    double ndof;
    double chi2;
    int ntracks;
    bool fake;
    bool valid;
  };
  */

  struct Vertices {
    Vertices() {}

    void book(TTree *tree, const std::string& prefix) {
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
   }

    void append(const reco::Vertex& vertex) {
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

      double sumpt_=0, sumpt2_=0;
      for(auto iTrack = vertex.tracks_begin(); iTrack != vertex.tracks_end(); ++iTrack) {
        if((*iTrack).isNonnull()) {
          const auto pt = (*iTrack)->pt();
          sumpt_ += pt;
          sumpt2_ += pt*pt;
        }
      }
      sumpt.push_back(sumpt_);
      sumpt2.push_back(sumpt2_);
    }

    void reset() {
      x.clear(); y.clear(); z.clear(); rho.clear();
      x_error.clear(); y_error.clear(); z_error.clear();
      ndof.clear(); chi2.clear(); ntracks.clear();
      sumpt.clear(); sumpt2.clear();
      fake.clear(); valid.clear();
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
  };

  Vertices b_pv;

  Vertices b_res_vertex1;
  int b_res_vertex1_tracks_size;
  Vertices b_res_vertex2;
  int b_res_vertex2_tracks_size;

  Vertices b_eff_vertexTag;
  int b_eff_vertexTag_tracks_size;
  Vertices b_eff_vertexProbe;
  int b_eff_vertexProbe_tracks_size;
};

VertexPerformanceNtuple::VertexPerformanceNtuple(const edm::ParameterSet& iConfig):
  vertexSrc_(consumes<reco::VertexCollection>(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc"))),
  beamspotSrc_(consumes<reco::BeamSpot>(iConfig.getUntrackedParameter<edm::InputTag>("beamspotSrc")))
{
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
}

VertexPerformanceNtuple::~VertexPerformanceNtuple() {}

void VertexPerformanceNtuple::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.addUntracked<edm::InputTag>("vertexSrc", edm::InputTag("offlinePrimaryVertices"));
  desc.addUntracked<edm::InputTag>("beamspotSrc", edm::InputTag("offlineBeamSpot"));

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

  tree->Branch("nvertices", &b_nvertices);
  tree->Branch("nvertices_good", &b_nvertices_good);

  b_pv.book(tree, "pv");

  b_res_vertex1.book(tree, "res_vertex1");
  tree->Branch("res_vertex1_tracks_size", &b_res_vertex1_tracks_size);

  b_res_vertex2.book(tree, "res_vertex2");
  tree->Branch("res_vertex2_tracks_size", &b_res_vertex2_tracks_size);

  b_eff_vertexTag.book(tree, "eff_vertexTag");
  tree->Branch("eff_vertexTag_tracks_size", &b_eff_vertexTag_tracks_size);

  b_eff_vertexProbe.book(tree, "eff_vertexProbe");
  tree->Branch("eff_vertexProbe_tracks_size", &b_eff_vertexProbe_tracks_size);

  reset();
}

void VertexPerformanceNtuple::reset() {
  b_run=0; b_lumi=0; b_event=0;
  b_nvertices=0; b_nvertices_good=0;
  b_pv.reset();

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
  edm::Handle<reco::VertexCollection> hvertices;
  iEvent.getByToken(vertexSrc_, hvertices);
  const reco::VertexCollection& vertices = *hvertices;

  edm::Handle<reco::BeamSpot> hbeamspot;
  iEvent.getByToken(beamspotSrc_, hbeamspot);
  const reco::BeamSpot& beamspot = *hbeamspot;

  edm::ESHandle<TransientTrackBuilder> ttBuilderHandle;
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", ttBuilderHandle);
  const TransientTrackBuilder& ttBuilder = *ttBuilderHandle;

  edm::Service<edm::RandomNumberGenerator> rng;
  CLHEP::HepRandomEngine& engine = rng->getEngine(iEvent.streamID());

  b_run = iEvent.id().run();
  b_lumi = iEvent.id().luminosityBlock();
  b_event = iEvent.id().event();

  b_nvertices = vertices.size();
  b_nvertices_good = 0;
  for(const auto& v: vertices) {
    if(v.ndof() >= 4)
      ++b_nvertices_good;
  }

  if(!vertices.empty()) {
    // For now, do it only for "the PV"
    const reco::Vertex& thePV = vertices[0];
    b_pv.append(thePV);

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

      doResolution(ttracks, engine);
      if(thePV.tracksSize() >= 6) {
        doEfficiency(ttracks, engine);
      }
    }
  }
  tree->Fill();
  reset();
}

void VertexPerformanceNtuple::doResolution(const std::vector<reco::TransientTrack>& ttracks, CLHEP::HepRandomEngine& engine) {
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

  b_res_vertex1_tracks_size = set1.size();
  b_res_vertex2_tracks_size = set2.size();

  // For resolution we only fit
  TransientVertex vertex1 = fitter_.vertex(set1);
  TransientVertex vertex2 = fitter_.vertex(set2);

  edm::LogVerbatim("VertexPerformanceNtuple") << "Set1: " << set1.size() << " tracks, vertex " << (vertex1.isValid() ? "valid " : "invalid ") << vertex1.position();
  edm::LogVerbatim("VertexPerformanceNtuple") << "Set2: " << set2.size() << " tracks, vertex " << (vertex2.isValid() ? "valid " : "invalid ") << vertex2.position();

  b_res_vertex1.append(vertex1);
  b_res_vertex2.append(vertex2);
}

void VertexPerformanceNtuple::doEfficiency(const std::vector<reco::TransientTrack>& tracks, CLHEP::HepRandomEngine& engine) {
  // 2/3 for tag, 1/3 for probe
  std::vector<reco::TransientTrack> setTag, setProbe;
  setTag.reserve(2*tracks.size()/3+1); setProbe.reserve(tracks.size()/3+1);

  const size_t end = tracks.size() - tracks.size()%3;
  for(size_t i=0; i<end; i+= 3) {
    const size_t probe_i = CLHEP::RandFlat::shootInt(&engine, 0, 3);
    setProbe.push_back(tracks[i+probe_i]);

    for(size_t j=0; j<3; ++j) {
      if(j == probe_i) continue;
      setTag.push_back(tracks[i+probe_i]);
    }
  }
  if(tracks.size()%3 == 1) {
    setTag.push_back(tracks[end]);
  }
  else if(tracks.size()%3 == 2) {
    const size_t probe_i = CLHEP::RandFlat::shootInt(&engine, 0, 2);
    const size_t tag_i = 1-probe_i;
    setProbe.push_back(tracks[end+probe_i]);
    setTag.push_back(tracks[end+tag_i]);
  }

  b_eff_vertexTag_tracks_size = setTag.size();
  b_eff_vertexProbe_tracks_size = setProbe.size();

  // Here we also cluster in addition to fit
  std::vector< std::vector<reco::TransientTrack> > && clustersTag =  clusterizer_->clusterize(setTag);
  std::vector< std::vector<reco::TransientTrack> > && clustersProbe =  clusterizer_->clusterize(setProbe);
  edm::LogVerbatim("VertexPerformanceNtuple") << "SetTag: " << setTag.size() << " tracks, " << clustersTag.size() << " clusters";
  for(const auto& cluster: clustersTag) {
    TransientVertex vertex = fitter_.vertex(cluster);
    b_eff_vertexTag.append(vertex);
    
    edm::LogVerbatim("VertexPerformanceNtuple") << " vertex " << (vertex.isValid() ? "valid " : "invalid ") << vertex.position();
  }

  edm::LogVerbatim("VertexPerformanceNtuple") << "SetProbe: " << setProbe.size() << " tracks, " << clustersProbe.size() << " clusters";
  for(const auto& cluster: clustersProbe) {
    TransientVertex vertex = fitter_.vertex(cluster);
    b_eff_vertexProbe.append(vertex);
    edm::LogVerbatim("VertexPerformanceNtuple") << " vertex " << (vertex.isValid() ? "valid " : "invalid ") << vertex.position();
  }

}

DEFINE_FWK_MODULE(VertexPerformanceNtuple);

