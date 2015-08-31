from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'vtx_singlemu_v1'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
#config.JobType.maxMemoryMB = 2500
config.JobType.psetName    = 'step3.py'

config.section_("Data")
config.Data.inputDataset = '/RelValTTbar_13/CMSSW_7_6_0_pre3-75X_mcRun2_asymptotic_v2-v1/GEN-SIM-DIGI-RAW-HLTDEBUG'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 2000
config.Data.outLFNDirBase = '/store/group/cmst3/user/mkortela/crab/vertexPerformance_74x'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
config.Site.whitelist = ["T2_CH_CERN"]
