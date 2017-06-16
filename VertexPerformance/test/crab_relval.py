from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'RelValMinBias_8020_Tranche4GT_v2'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
#config.JobType.maxMemoryMB = 2500
config.JobType.psetName    = 'config_relval.py'

config.section_("Data")
config.Data.inputDataset = '/RelValMinBias_13/CMSSW_8_0_20-80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/GEN-SIM-RECO'
config.Data.useParent = True
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/cmst3/user/mkortela/crab/vertexPerformance_80x/vtx_relvalminbias_v1'
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = ["T2_CH_CERN"]

