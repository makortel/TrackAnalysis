#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TH1F.h"
#include "TNamed.h"

#include<limits>
#include<string>

class VertexPerformanceConfigInfo: public edm::one::EDAnalyzer<edm::one::SharedResources> {
 public:
  explicit VertexPerformanceConfigInfo(const edm::ParameterSet&);
  ~VertexPerformanceConfigInfo();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

 private:
  virtual void analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) override;
  virtual void endJob() override;

private:
  std::string dataVersion;
  std::string codeVersion;
  std::string era;
  unsigned energy;
};

VertexPerformanceConfigInfo::VertexPerformanceConfigInfo(const edm::ParameterSet& pset): 
  dataVersion(pset.getUntrackedParameter<std::string>("dataVersion")),
  codeVersion(pset.getUntrackedParameter<std::string>("codeVersion")),
  era(pset.getUntrackedParameter<std::string>("era")),
  energy(pset.getUntrackedParameter<unsigned>("energy"))
{}

VertexPerformanceConfigInfo::~VertexPerformanceConfigInfo() {}

void VertexPerformanceConfigInfo::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.addUntracked<std::string>("dataVersion", "");
  desc.addUntracked<std::string>("codeVersion", "");
  desc.addUntracked<std::string>("era", "");
  desc.addUntracked<unsigned>("energy", 0);

  descriptions.add("vertexPerformanceConfigInfo", desc);
}

void VertexPerformanceConfigInfo::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {}

void VertexPerformanceConfigInfo::endJob() {
  edm::Service<TFileService> fs;

  TH1F *info = fs->make<TH1F>("configinfo", "configinfo", 2, 0, 2);

  int bin = 1;
  info->GetXaxis()->SetBinLabel(bin, "control");
  info->AddBinContent(bin, 1);
  ++bin;

  info->GetXaxis()->SetBinLabel(bin, "energy");
  info->AddBinContent(bin, energy);
  ++bin;

  fs->make<TNamed>("dataVersion", dataVersion.c_str());
  fs->make<TNamed>("codeVersion", codeVersion.c_str());
  if(era.length() > 0)
    fs->make<TNamed>("era", era.c_str());
}

//define this as a plug-in
DEFINE_FWK_MODULE(VertexPerformanceConfigInfo);
