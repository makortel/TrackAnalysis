from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'SingleMuon_254790_v2'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
#config.JobType.maxMemoryMB = 2500
config.JobType.psetName    = 'config.py'

config.section_("Data")
config.Data.inputDataset = '/SingleMuon/Run2015C-PromptReco-v1/AOD'
config.Data.lumiMask = 'json_run_254790.txt'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 100000
#config.Data.outLFNDirBase = baseDir
config.Data.outLFNDirBase = '/store/group/cmst3/user/mkortela/crab/vertexPerformance_74x/vtx_singlemuon_v1'
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = ["T2_CH_CERN"]

