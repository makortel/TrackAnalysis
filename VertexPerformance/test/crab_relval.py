from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'RelValZMM_50ns_746p6_noCCCv3_v2'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
#config.JobType.maxMemoryMB = 2500
config.JobType.psetName    = 'config_relval.py'

config.section_("Data")
config.Data.inputDataset = '/RelValZMM_13/CMSSW_7_4_6_patch6-PU50ns_MCRUN2_74_V8_unsch_noCCC_v3-v1/GEN-SIM-RECO'
config.Data.useParent = True
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/cmst3/user/mkortela/crab/vertexPerformance_74x/vtx_relvalzmm_v1'
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = ["T2_CH_CERN"]

