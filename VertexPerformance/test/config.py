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
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing()
options.register("globalTag", "80X_dataRun2_Prompt_v9",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "GlobalTag to use")
options.parseArguments()

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(1000)
    input = cms.untracked.int32(10000)
)

process.MessageLogger.cerr.FwkReport.reportEvery = 500
process.MessageLogger.suppressWarning.append("vertexPerformanceNtuple")
#process.MessageLogger.categories.append("TwoTrackMinimumDistance")
#process.MessageLogger.cerr.TwoTrackMinimumDistance = cms.untracked.PSet(limit = cms.untracked.int32(10))

# In RelVals
# 2012D: 208307
# 2015B: 251251
# 2015C: 254790
# 2015D: 256677

# dataset=/RelValMinBias_13/CMSSW_7_4_8_patch1-MCRUN2_74_V11_mulTrh-v1/GEN-SIM-RECO
files_minbias_mc = [
    "/store/relval/CMSSW_7_4_8_patch1/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_74_V11_mulTrh-v1/00000/10FCD2FE-533C-E511-A2C4-003048FFD752.root",
    "/store/relval/CMSSW_7_4_8_patch1/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_74_V11_mulTrh-v1/00000/6005E242-5C3C-E511-B4A5-0025905A48BB.root",
    "/store/relval/CMSSW_7_4_8_patch1/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_74_V11_mulTrh-v1/00000/8CBA4B55-543C-E511-9BCB-0026189438E1.root",
    "/store/relval/CMSSW_7_4_8_patch1/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_74_V11_mulTrh-v1/00000/9A8C9904-543C-E511-8A7D-0025905A60CE.root",
    "/store/relval/CMSSW_7_4_8_patch1/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_74_V11_mulTrh-v1/00000/A41F35A9-533C-E511-B0A6-0025905A605E.root",
    "/store/relval/CMSSW_7_4_8_patch1/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_74_V11_mulTrh-v1/00000/C43B613D-5C3C-E511-950C-0025905A6122.root",
]

# 25ns
# file dataset=/SingleMuon/Run2015C-PromptReco-v1/AOD run=254833
files_singlemu_run254790 = [
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/06E09600-244A-E511-9495-02163E014123.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/08455FBD-2D4A-E511-A872-02163E0143EF.root",
]
golden_run254790 = [
    "254790:90",
    "254790:93-254790:208",
    "254790:344-254790:602",
    "254790:608-254790:630",
    "254790:633-254790:665",
    "254790:782-254790:784",
]

# 50ns
files_singlemu_run254833 = [
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/04FCF762-134B-E511-A5CF-02163E0146D7.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/0645B1B1-104B-E511-95F5-02163E01449E.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/0C6FD3C8-104B-E511-A962-02163E013883.root",

]

# file dataset=/JetHT/Run2015B-16Oct2015-v1/AOD run=251251
files_jetht_run251251 = [
"/store/data/Run2015B/JetHT/AOD/16Oct2015-v1/20000/0816697E-8579-E511-AE38-0025905A6132.root",
"/store/data/Run2015B/JetHT/AOD/16Oct2015-v1/20000/26083A0C-8579-E511-9706-0025905B859E.root",
"/store/data/Run2015B/JetHT/AOD/16Oct2015-v1/20000/2CEDF9F2-8479-E511-A00C-0025905A610C.root",
"/store/data/Run2015B/JetHT/AOD/16Oct2015-v1/20000/2E20CC24-8379-E511-A4F1-003048FFD796.root",
]
golden_run251251 = [
    "251251:1-251251:31",
    "251251:33-251251:97",
    "251251:99-251251:167",
]

# file dataset=/JetHT/Run2016B-PromptReco-v2/AOD run=273725
files_jetht_run273725 = [
    "/store/data/Run2016B/JetHT/AOD/PromptReco-v2/000/273/725/00000/001837B2-7D20-E611-B10B-02163E011B2D.root",
    "/store/data/Run2016B/JetHT/AOD/PromptReco-v2/000/273/725/00000/10A36775-8F20-E611-801D-02163E012143.root",
    "/store/data/Run2016B/JetHT/AOD/PromptReco-v2/000/273/725/00000/2A022476-8B20-E611-9E4F-02163E01341C.root",
]
golden_run273725 = [
    "273725:83-273725:252",
    "273725:254-273725:2545",
]


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
)
#process.source.fileNames = files_singlemu_run254790 # 25ns
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(golden_run254790)
#process.source.fileNames = files_jetht_run251251
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(golden_run251251)
#process.source.fileNames = files_jetht_run273725
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(golden_run273725)

#process.source.fileNames = ["/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/0E860294-1C4A-E511-B501-02163E011955.root"]
#process.maxEvents.input = -1
#process.source.lumisToProcess = ["254790:169-254790:170"]
#process.source.lumisToProcess = ["254790:170"]
#del process.source.lumisToProcess
#process.source.eventsToProcess = cms.untracked.VEventRange("254790:170:206530637")

#process.source.fileNames = files_jetht_run273725
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(golden_run273725)

process.options = cms.untracked.PSet()


from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '74X_dataRun2_Prompt_v1', '')
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')
#print process.GlobalTag.globaltag.value()


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
process.vertexPerformanceNtuple.TkClusParameters = cms.untracked.PSet(**process.unsortedOfflinePrimaryVertices.TkClusParameters.parameters_())
#process.vertexPerformanceNtuple.triggerResultsSrc.setProcessName("HLT2") # for newcond RelVal
process.vertexPerformanceNtuple.triggers = [
    "HLT_PFHT800_v1",
    "HLT_PFHT800_v2",
    "HLT_PFHT800_v3",
    "HLT_PFHT800_v4"
]
#process.vertexPerformanceNtuple.minimal = True

process.load("TrackAnalysis/VertexPerformance/vertexPerformanceConfigInfo_cfi")
process.configInfo = process.vertexPerformanceConfigInfo.clone(
    dataVersion = "80xdata",
    codeVersion = getCommitId(),
    energy = 13
)
process.p = cms.Path(
    process.vertexPerformanceNtuple+
    process.configInfo
)
