import time
import subprocess
from multiprocessing import Process

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from WMCore.Configuration import Configuration
from httplib import HTTPException

#multitaskdir = 'vtx_singlemuon_v2'
#multitaskdir = 'vtx_jetht_v11_2'
multitaskdir = 'vtx_zerobias_v3_1'
#multitaskdir = 'vtx_jetht_doublemuon_v4'
baseDir = '/store/group/cmst3/user/mkortela/crab/vertexPerformance_80x/'+multitaskdir
eosDir = '/eos/cms'+baseDir

eos = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select'

def _execute(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (output, error) = p.communicate()
    return p.returncode
def _executeThrow(cmd):
    ret = _execute(cmd)    
    if ret != 0:
        raise Exception("Ran '%s', got exitcode with output\n%s\n%s" % (" ".join(cmd), ret, output, error))
    print "Created eos dir", eosDir


# https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/622/1/1/2/1/1/1/1.html
def submit_(config):
    try:
        args = [
#            "--dryrun", "--skip-estimates"
        ]
        crabCommand('submit', config = config, *args)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

def submit(config):
    p = Process(target=submit_, args=(config,))
    p.start()
    p.join()

def main():
    if _execute([eos, "ls", eosDir]) != 0:
        _executeThrow([eos, "mkdir", eosDir])

    config = Configuration()

    config.section_("General")
    
    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    #config.General.workArea = 'multicrab_'+time.strftime("%y%m%d_%H%M%S")
    config.General.workArea = multitaskdir+"_"+time.strftime("%y%m%d_%H%M%S")

    config.section_("General")
    config.General.transferLogs = True

    config.section_("JobType")
    config.JobType.pluginName  = 'Analysis'
    config.JobType.psetName    = 'config.py'

    config.section_("Data")
    config.Data.inputDataset = 'Dummy'
    config.Data.splitting = 'EventAwareLumiBased'
    #config.Data.unitsPerJob = 100000
    config.Data.unitsPerJob = 1000000
#    config.Data.unitsPerJob = 500000  # for full stats
    config.Data.outLFNDirBase = baseDir
    config.Data.publication = False

    config.section_("Site")
    config.Site.storageSite = 'T2_CH_CERN'
    #config.Site.whitelist = ["T2_CH_CERN"]
    #config.Site.whitelist = ["T3_CH_CERN_CAF"]

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

#    config.General.requestName = 'JetHT_Run2015B_251251'
#    config.Data.inputDataset = "/JetHT/Run2015B-16Oct2015-v1/AOD"
#    config.Data.lumiMask = 'json_run_251251.txt'
#    config.JobType.pyCfgParams = ["globalTag=74X_dataRun2_v4"]
#    submit(config)
#
#    config.General.requestName = 'JetHT_Run2015C_254790'
#    config.Data.inputDataset = "/JetHT/Run2015C_25ns-05Oct2015-v1/AOD"
#    config.Data.lumiMask = 'json_run_254790.txt'
#    config.JobType.pyCfgParams = ["globalTag=74X_dataRun2_v4"]
#    submit(config)
#
#    config.General.requestName = 'JetHT_Run2015D_256677'
#    config.Data.inputDataset = "/JetHT/Run2015D-PromptReco-v3/AOD"
#    config.Data.lumiMask = 'json_run_256677.txt'
#    config.JobType.pyCfgParams = ["globalTag=74X_dataRun2_Prompt_v2"]
#    submit(config)

#    config.General.requestName = 'JetHT_Run2015C_254833'
#    config.Data.inputDataset = "/JetHT/Run2015C-PromptReco-v1/AOD"
#    config.Data.lumiMask = 'json_run_254833.txt'
#    config.JobType.pyCfgParams = ["globalTag=74X_dataRun2_v4"]
#    submit(config)

#    config.General.requestName = 'JetHT_Run2016B_273725'
#    config.Data.inputDataset = "/JetHT/Run2016B-PromptReco-v2/AOD"
#    config.Data.lumiMask = 'json_run_273725.txt'
#    config.JobType.pyCfgParams = ["globalTag=80X_dataRun2_Prompt_v9"]
#    submit(config)

#    config.General.requestName = 'JetHT_Run2016B_274160'
#    config.Data.inputDataset = "/JetHT/Run2016B-PromptReco-v2/AOD"
#    config.Data.lumiMask = 'json_run_274160.txt'
#    config.JobType.pyCfgParams = ["globalTag=80X_dataRun2_Prompt_v9"]
#    submit(config)

#    config.General.requestName = 'JetHT_Run2016B_274199'
#    config.Data.inputDataset = "/JetHT/Run2016B-PromptReco-v2/AOD"
#    config.Data.lumiMask = 'json_run_274199.txt'
#    config.JobType.pyCfgParams = ["globalTag=80X_dataRun2_Prompt_v9"]
#    submit(config)

#    config.General.requestName = 'JetHT_Run2016B_274199_newcond'
#    config.Data.inputDataset = "/JetHT/CMSSW_8_0_14-80X_dataRun2_relval_v15_RelVal_jetHT2016B-v1/RECO"
#    config.Data.lumiMask = 'json_run_274199.txt'
#    config.JobType.pyCfgParams = ["globalTag=80X_dataRun2_relval_v15"]
#    submit(config)

#    config.General.requestName = 'DoubleMuon_Run2016B_274160'
#    config.Data.inputDataset = "/DoubleMuon/Run2016B-PromptReco-v2/AOD"
#    config.Data.lumiMask = 'json_run_274160.txt'
#    config.JobType.pyCfgParams = ["globalTag=80X_dataRun2_Prompt_v9"]
#    submit(config)

#    config.General.requestName = 'DoubleMuon_Run2016B_274160_newcond'
#    config.Data.inputDataset = "/DoubleMuon/CMSSW_8_0_8_patch1-2016_06_07_HLTnewconditions0_80X_dataRun2_HLTValidation_forPostTS1_2016_v1-v1/RECO"
#    config.Data.lumiMask = 'json_run_274160.txt'
#    config.JobType.pyCfgParams = ["globalTag=80X_dataRun2_PromptValidation_forPostTS1_2016_v1"]
#    submit(config)

#    config.General.requestName = 'JetHT_Run2016B_v2'
#    config.Data.inputDataset = "/JetHT/Run2016B-PromptReco-v2/AOD"
#    config.Data.lumiMask = 'Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt'
#    config.Data.unitsPerJob = 500000
#    config.JobType.pyCfgParams = ["globalTag=80X_dataRun2_Prompt_v9"]
#    submit(config)


    # works better for the ZeroBias
    config.Data.splitting = 'LumiBased'
    config.Data.unitsPerJob = 20

    #for zb in ["ZeroBias"] + ["ZeroBias%d" % x for x in xrange(0, 9)]:
    #for zb in ["ZeroBias"] + ["ZeroBias%d" % x for x in xrange(1, 9)]:
    for zb in ["ZeroBias%d" % x for x in xrange(1, 9)]:
        config.General.requestName = '%s_Run2016B_274100' % zb
        config.Data.inputDataset = "/%s/Run2016B-PromptReco-v2/RECO" % zb
        config.Data.lumiMask = 'json_run_274100.txt'
        config.JobType.pyCfgParams = ["globalTag=80X_dataRun2_Prompt_v9"]
        submit(config)


if __name__ == '__main__':
    main()
