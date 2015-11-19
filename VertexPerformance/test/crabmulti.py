import time
import subprocess

multitaskdir = 'vtx_singlemuon_v2'
baseDir = '/store/group/cmst3/user/mkortela/crab/vertexPerformance_74x/'+multitaskdir
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


def main():
    if _execute([eos, "ls", eosDir]) != 0:
        _executeThrow([eos, "mkdir", eosDir])

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from WMCore.Configuration import Configuration
    from httplib import HTTPException

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
    config.Data.inputDataset = '/SingleMuon/Run2015C-PromptReco-v1/AOD'
    config.Data.splitting = 'EventAwareLumiBased'
    config.Data.unitsPerJob = 50000
    config.Data.outLFNDirBase = baseDir
    config.Data.publication = False

    config.section_("Site")
    config.Site.storageSite = 'T2_CH_CERN'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    config.General.requestName = 'SingleMuon_254790'
    config.Data.lumiMask = 'json_run_254790.txt'
    submit(config)

    config.General.requestName = 'SingleMuon_254833'
    config.Data.lumiMask = 'json_run_254833.txt'
    submit(config)

if __name__ == '__main__':
    main()
