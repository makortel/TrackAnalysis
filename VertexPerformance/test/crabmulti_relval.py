import time
import subprocess
from multiprocessing import Process

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from WMCore.Configuration import Configuration
from httplib import HTTPException

multitaskdir = 'vtx_ttbar_25ns_v1'
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
    config.JobType.psetName    = 'config_relval.py'

    config.section_("Data")
    config.Data.inputDataset = 'Dummy'
    config.Data.useParent = True
    config.Data.splitting = 'FileBased'
    config.Data.unitsPerJob = 1
    config.Data.outLFNDirBase = baseDir
    config.Data.publication = False

    config.section_("Site")
    config.Site.storageSite = 'T2_CH_CERN'

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    config.General.requestName = 'RelValTTbar_25ns_810'
    config.Data.inputDataset = "/RelValTTbar_13/CMSSW_8_0_10-PU25ns_80X_mcRun2_asymptotic_v14-v1/GEN-SIM-RECO"
    config.JobType.pyCfgParams = ["globalTag=80X_mcRun2_asymptotic_v14"]
    submit(config)

    config.General.requestName = 'RelValTTbar_25ns_810p1_BS'
    config.Data.inputDataset = "/RelValTTbar_13/CMSSW_8_0_10_patch1-PU25ns_80X_mcRun2_asymptotic_RealisticBS_25ns_13TeV2016_v1_mc_realisticBS2016-v1/GEN-SIM-RECO"
    config.JobType.pyCfgParams = ["globalTag=80X_mcRun2_asymptotic_RealisticBS_25ns_13TeV2016_v1_mc"]
    submit(config)



if __name__ == '__main__':
    main()
