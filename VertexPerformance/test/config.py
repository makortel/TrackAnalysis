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

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

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
files_singlemu_run254790 = [
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/06E09600-244A-E511-9495-02163E014123.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/08455FBD-2D4A-E511-A872-02163E0143EF.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/0AAF82EF-204A-E511-8839-02163E01458E.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/0E860294-1C4A-E511-B501-02163E011955.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/1E6693F3-404A-E511-BFB8-02163E01412C.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/1E87BA35-2A4A-E511-9153-02163E011EAC.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/2EF2CC0E-1E4A-E511-B402-02163E0145C1.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/54AE483B-254A-E511-9406-02163E013665.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/5880A4EA-254A-E511-A3F7-02163E0138D8.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/82516E61-2B4A-E511-82D5-02163E011EDC.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/9CA65BA8-284A-E511-A6BF-02163E0139CB.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/A2FF1851-224A-E511-9C85-02163E01359A.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/B2FB4E7E-264A-E511-AB20-02163E013557.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/B8E9EA73-234A-E511-BF21-02163E014176.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/D0E7AF8E-324A-E511-A25E-02163E0134DC.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/D68982F9-1F4A-E511-B323-02163E01380A.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/DC144185-2B4A-E511-970D-02163E014648.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/DC9A4738-2D4A-E511-9271-02163E011A31.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/E0D153B0-274A-E511-8CB2-02163E011954.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/E2AB1BA1-244A-E511-B57D-02163E013472.root",
    "/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/790/00000/E2CE491E-2E4A-E511-BBE1-02163E013624.root",
]

# 50ns
files_singlemu_run254833 = [
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/04FCF762-134B-E511-A5CF-02163E0146D7.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/0645B1B1-104B-E511-95F5-02163E01449E.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/0C6FD3C8-104B-E511-A962-02163E013883.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/0CF6FDB2-104B-E511-AA64-02163E0144BE.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/10FA81C7-104B-E511-8463-02163E011815.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/1605F1B0-104B-E511-905F-02163E013726.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/160F9BB6-104B-E511-937F-02163E01389F.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/186B7ABF-104B-E511-9F53-02163E011FE6.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/1891C4C2-104B-E511-9DA6-02163E012750.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/1A5D78BE-104B-E511-B0C8-02163E013761.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/2A9B75BE-104B-E511-93EA-02163E01345E.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/2C263DD8-104B-E511-952C-02163E012A1F.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/36C5A9AE-104B-E511-9AD9-02163E0146B0.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/3EF6A7C7-104B-E511-BBAA-02163E012A1F.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/4284CFC7-104B-E511-9B97-02163E012A1F.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/4475E0C8-104B-E511-8D65-02163E013883.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/46A869B5-104B-E511-85E8-02163E012ABA.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/4A4292DA-104B-E511-8C84-02163E013456.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/4A4F5DBC-104B-E511-900B-02163E011DE4.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/62E9E7C5-104B-E511-BB8E-02163E0125EF.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/64D5D8BE-104B-E511-9ACF-02163E0144B4.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/680FFBB8-104B-E511-9486-02163E01248D.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/6C73ACB3-104B-E511-B827-02163E0143FF.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/724218B4-104B-E511-9D82-02163E01369A.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/76EF71BD-104B-E511-9957-02163E0124C0.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/783E6BBE-104B-E511-BB2D-02163E0120E5.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/82B14EB8-104B-E511-B95A-02163E0145BB.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/842988B4-104B-E511-B57A-02163E01454C.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/86985CCE-104B-E511-B572-02163E013443.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/86C246BA-104B-E511-85EA-02163E0134B1.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/8AC7F3BD-104B-E511-87C9-02163E0120E5.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/9422D4B4-104B-E511-BD16-02163E0137D0.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/9E0F93BD-104B-E511-B686-02163E01452A.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/A66EB3B8-104B-E511-892D-02163E011A51.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/AE3FC5AF-104B-E511-9A4A-02163E014111.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/B2AC50B3-104B-E511-B01B-02163E011D3C.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/BAAFABC0-104B-E511-A3E3-02163E01343E.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/BEADAEB6-104B-E511-820D-02163E01342D.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/C216D9BA-104B-E511-AD25-02163E0141E1.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/C60B02C1-104B-E511-9463-02163E01435E.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/CE3758BE-104B-E511-9D46-02163E0120E5.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/D029E6BE-104B-E511-947F-02163E011D28.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/D89C39BE-104B-E511-BBC2-02163E0120E5.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/E0E7F5C2-104B-E511-9A4A-02163E013776.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/EC9369B5-104B-E511-9F6A-02163E012ABA.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/EEED98C0-104B-E511-9EDA-02163E011CBE.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/F08927C1-104B-E511-AC4B-02163E014336.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/F40AC1CF-104B-E511-A94C-02163E0139AE.root",
"/store/data/Run2015C/SingleMuon/AOD/PromptReco-v1/000/254/833/00000/FE2633B5-104B-E511-A94F-02163E01445A.root",
]


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
)
process.source.fileNames = files_singlemu_run254790

process.options = cms.untracked.PSet()


from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '74X_dataRun2_Prompt_v1', '')

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("histograms.root")
)


process.RandomNumberGeneratorService.vertexPerformanceNtuple = cms.PSet(
    initialSeed = cms.untracked.uint32(1234),
    engineName = cms.untracked.string("HepJamesRandom")
)

process.load("TrackAnalysis/VertexPerformance/vertexPerformanceNtuple_cfi")
process.vertexPerformanceNtuple.TkClusParameters = cms.untracked.PSet(**process.unsortedOfflinePrimaryVertices.TkClusParameters.parameters_())
process.load("TrackAnalysis/VertexPerformance/vertexPerformanceConfigInfo_cfi")
process.configInfo = process.vertexPerformanceConfigInfo.clone(
)
process.p = cms.Path(
    process.vertexPerformanceNtuple+
    process.configInfo
)
