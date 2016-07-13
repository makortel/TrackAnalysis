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
options.register("globalTag", "80X_mcRun2_asymptotic_v14",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "GlobalTag to use")
options.parseArguments()

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(-1)
    input = cms.untracked.int32(100)
)

# dataset=/RelValZMM_13/CMSSW_7_4_6_patch6-PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/GEN-SIM-RECO
files_zmm_mc = [
    "/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/0430B317-0C2C-E511-B167-0026189438FA.root",
    "/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/34E37A7E-0E2C-E511-8799-00259059391E.root",
    "/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/3E60FDD4-0D2C-E511-838E-0025905A609E.root",
    "/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/92D4489B-0B2C-E511-AD8D-002618943919.root",
    "/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/B4AF50A5-0B2C-E511-96A7-0025905A48BB.root",
    "/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/CCC3B8E3-102C-E511-9E70-002590596486.root",
    "/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/D865E86E-0C2C-E511-AD09-0026189437EB.root",
]
files_zmm_mc_digi = [
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/020D4A30-E62B-E511-BA04-0025905938D4.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/140F99DD-E42B-E511-9C85-0025905A608C.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/1681D3AB-E52B-E511-B8CC-0025905B857C.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/1C5C42AC-E52B-E511-BCFC-0025905A6088.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/1EF55071-E52B-E511-BBFD-0025905A610C.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/22FC17B8-E52B-E511-AA68-0025905A60A0.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/26870AF2-E32B-E511-A60E-0025905964CC.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/2AFD9478-E52B-E511-B788-0025905B85AE.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/2CED7677-E52B-E511-9B55-00259059391E.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/3CB1D670-E52B-E511-9151-0025905A6056.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/40ECA76F-E52B-E511-B3A3-0025905A48F0.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/4C0448F3-E32B-E511-B620-002618943833.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/4EA75EFB-E32B-E511-B187-003048FFD71E.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/523A9F8F-E62B-E511-B16E-0025905A6088.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/6AF6542E-E62B-E511-9F4D-003048FFD75C.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/7A19CA6D-E52B-E511-BFAE-0025905B855E.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/8E8A7AE3-E42B-E511-9715-0025905964BA.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/9A2EE0DC-E42B-E511-B3BE-0025905A6134.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/9C68D3AC-E52B-E511-A2AE-0025905A48EC.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/B2C88835-E62B-E511-9C52-0025905A7786.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/E2BAAFEE-E32B-E511-BE71-0025905A60FE.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/E61075DD-E42B-E511-A8B4-0025905A60AA.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/E8E2F3AC-E52B-E511-9465-0025905A60F4.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/EC233671-E52B-E511-9ACF-0025905A60BC.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/EEAE1EDE-E42B-E511-9510-0025905B85D0.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/F410288E-E62B-E511-82ED-0025905B8596.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/F435A9AC-E52B-E511-80B5-0025905A60A6.root",
"/store/relval/CMSSW_7_4_6_patch6/RelValZMM_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/00000/F4498A71-E52B-E511-98CC-0025905A48D8.root",
]


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
)
process.source.fileNames = files_zmm_mc
process.source.secondaryFileNames = cms.untracked.vstring(*files_zmm_mc_digi)
# golden json
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange("254790:90",
#                                                                    "254790:93-254790:208",
#                                                                    "254790:344-254790:602",
#                                                                    "254790:608-254790:630",
#                                                                    "254790:633-254790:665",
#                                                                    "254790:782-254790:784",
#)

#process.source.fileNames = ["/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/0E860294-1C4A-E511-B501-02163E011955.root"]
#process.maxEvents.input = -1
#process.source.lumisToProcess = ["254790:169-254790:170"]
#process.source.lumisToProcess = ["254790:170"]
#del process.source.lumisToProcess
#process.source.eventsToProcess = cms.untracked.VEventRange("254790:170:206530637")


process.options = cms.untracked.PSet()


from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')


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
process.vertexPerformanceNtuple.triggers = ["HLT_IsoMu20_v1"]
process.vertexPerformanceNtuple.useTrackingParticles = True

process.load("TrackAnalysis/VertexPerformance/vertexPerformanceConfigInfo_cfi")
process.configInfo = process.vertexPerformanceConfigInfo.clone(
    dataVersion = "80xmc",
    codeVersion = getCommitId(),
    energy = 13
)
process.p = cms.Path(
    process.vertexPerformanceNtuple+
    process.configInfo
)
