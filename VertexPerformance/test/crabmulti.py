import time
import subprocess

multitaskdir = 'vtx_jetht_v4'
baseDir = '/store/group/cmst3/user/mkortela/crab/vertexPerformance_53x/'+multitaskdir
eosDir = '/eos/cms'+baseDir

eos = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select'

def _execute(cmd, getoutput=False):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (output, error) = p.communicate()
    if getoutput:
        return (p.returncode, output, error)
    else:
        return p.returncode
def _executeThrow(cmd):
    (ret, output, error) = _execute(cmd, getoutput=True)
    if ret != 0:
        raise Exception("Ran '%s', got exitcode %d with output\n%s\n%s" % (" ".join(cmd), ret, output, error))
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
    config.Data.inputDataset = 'Dummy'
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

#    config.General.requestName = 'JetHT_Run2012D_208307'
#    config.Data.inputDataset = '/JetHT/Run2012D-22Jan2013-v1/AOD'
#    config.Data.lumiMask = 'json_run_208307.txt'
#    config.JobType.pyCfgParams = ["globalTag=FT_53_V21_AN6"]
#    submit(config)

    config.General.requestName = 'Jet_Run2011B_177719'
    config.Data.inputDataset = '/Jet/Run2011B-12Oct2013-v1/AOD'
    config.Data.lumiMask = 'json_run_177719.txt'
    config.JobType.pyCfgParams = ["globalTag=FT_53_LV5_AN1"]
    submit(config)


if __name__ == '__main__':
    main()
