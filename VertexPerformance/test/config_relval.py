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
options.register("globalTag", "80X_mcRun2_asymptotic_2016_TrancheIV_v2",
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

# dataset=/RelValMinBias_13/CMSSW_8_0_20-80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/GEN-SIM-RECO
files_minbias_mc = [
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/244821BA-AF7A-E611-A9BB-0CC47A7C3430.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/32B096FD-BC7A-E611-B6C6-0CC47A4D76CC.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/34B5BAE6-AD7A-E611-B9F8-0025905A60CA.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/4074A462-AF7A-E611-A1D6-0025905A48BA.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/467F7798-AE7A-E611-8E71-0025905A6092.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/900310B4-BD7A-E611-B9AE-0CC47A4D769E.root",
]
files_minbias_mc_digi = [
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/0C960945-A77A-E611-92F3-0CC47A4C8EE2.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/0E92984E-A77A-E611-8693-0025905A6088.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/10853DA5-A77A-E611-AD61-0025905A609E.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/1CA8761F-A77A-E611-928B-0CC47A4C8E0E.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/20291150-A77A-E611-A76B-0CC47A7452D0.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/261686F7-A67A-E611-BB06-0CC47A7C35F8.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/2A96E6A3-A77A-E611-A1D4-0025905B85CA.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/42A36AFB-A67A-E611-8927-0CC47A4D763C.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/5E79ABF5-A67A-E611-A162-0CC47A7C3434.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/769FDA46-A77A-E611-9409-0CC47A4D76B2.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/A03B2A04-A77A-E611-88D3-003048FFD7CE.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/AEC02BFC-A67A-E611-BE5A-0025905B856E.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/B2E945FB-A67A-E611-892B-0025905A6126.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/B86205FE-A67A-E611-A177-0025905A497A.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/C4275D57-A77A-E611-9E6C-0025905A613C.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/C44368F9-A67A-E611-89FC-0CC47A7C3636.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/CA0F0053-A77A-E611-92B3-0CC47A7C35A8.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/D2B41AFA-A67A-E611-A90E-0025905A605E.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/D2DFE3F6-A67A-E611-8FBC-0CC47A4C8E64.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/D40BA7FB-A67A-E611-B65F-0025905B85B2.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/D80FB3F6-A67A-E611-8618-0CC47A78A3EC.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/F0BC98FB-A67A-E611-B23F-0025905A6126.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/F8537318-A77A-E611-A2C4-0CC47A4C8E0E.root",
    "/store/relval/CMSSW_8_0_20/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/FC44D8FA-A67A-E611-A702-0025905A6094.root",
]


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
)
#process.source.fileNames = files_zmm_mc
#process.source.secondaryFileNames = cms.untracked.vstring(*files_zmm_mc_digi)
process.source.fileNames = files_minbias_mc
process.source.secondaryFileNames = cms.untracked.vstring(*files_minbias_mc_digi)

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
#process.vertexPerformanceNtuple.triggers = ["HLT_IsoMu20_v1"]
process.vertexPerformanceNtuple.useTrackingParticles = True
process.vertexPerformanceNtuple.minimal = True

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
