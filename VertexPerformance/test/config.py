import FWCore.ParameterSet.Config as cms

process = cms.Process('NTUPLE')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing()
options.register("globalTag", "FT_53_V21_AN6",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "GlobalTag to use")
options.parseArguments()


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# file dataset=/JetHT/Run2012D-22Jan2013-v1/AOD run=208307
files_jetht_run208307 = [
"/store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/04C7C47A-A692-E211-B13A-E0CB4E1A118D.root",
"/store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/0A15DA75-D892-E211-AF5B-E0CB4E1A1176.root",
"/store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/0AFEE85E-CA92-E211-A39E-E0CB4EA0A932.root",
"/store/data/Run2012D/JetHT/AOD/22Jan2013-v1/10000/0E009C74-D392-E211-A6B2-E0CB4E4408DF.root",
]
#golden_run208307 = [
#    "251251:1-251251:31",
#    "251251:33-251251:97",
#    "251251:99-251251:167",
#]


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
)
process.source.fileNames = files_jetht_run208307 # 25ns
# golden json
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(golden_run251251)

#process.source.fileNames = ["/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/0E860294-1C4A-E511-B501-02163E011955.root"]
#process.maxEvents.input = -1
#process.source.lumisToProcess = ["254790:169-254790:170"]
#process.source.lumisToProcess = ["254790:170"]
#del process.source.lumisToProcess
#process.source.eventsToProcess = cms.untracked.VEventRange("254790:170:206530637")


process.options = cms.untracked.PSet()


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag+'::All', '')


import subprocess
def getCommitId():
    cmd = ["git", "show", "--pretty=format:%H"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, error) = p.communicate()
    ret = p.returncode
    if ret != 0:
        raise Exception("Ran %s, got exit code %d with output\n%s\n%s" % (" ".join(cmd), ret, output, error))
    return output.split("\n")[0]

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("histograms.root")
)


process.RandomNumberGeneratorService.vertexPerformanceNtuple = cms.PSet(
    initialSeed = cms.untracked.uint32(1234),
    engineName = cms.untracked.string("HepJamesRandom")
)

process.load("TrackAnalysis/VertexPerformance/vertexPerformanceNtuple_cfi")
process.vertexPerformanceNtuple.TkClusParameters = cms.untracked.PSet(**process.offlinePrimaryVertices.TkClusParameters.parameters_())
#process.vertexPerformanceNtuple.triggers = ["HLT_IsoMu20_v2"]

process.load("TrackAnalysis/VertexPerformance/vertexPerformanceConfigInfo_cfi")
process.configInfo = process.vertexPerformanceConfigInfo.clone(
    dataVersion = "53xdata",
    codeVersion = getCommitId(),
    energy = 8
)
process.p = cms.Path(
    process.vertexPerformanceNtuple+
    process.configInfo
)
