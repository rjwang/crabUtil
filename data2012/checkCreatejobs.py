#!/usr/bin/env python
import os,sys
import getopt
import commands


ALLSCRIPT = open('script_createjobs.sh',"w")

allsubmits = 'All.cfg'
with open(allsubmits) as fp:
    lists = []
    for line in fp:
	if( ("[MC8TeV_" in line) or ("[Data8TeV_" in line) ):

	    line1 = line.split(']')[0]
	    setname = line1.split('[')[1]

	    ALLSCRIPT.writelines(' multicrab -create -cfg '+ 'Multicrab_'+setname+'.cfg \n')

	    SCRIPT = open('Multicrab_'+setname+'.cfg',"w")
            SCRIPT.writelines('[MULTICRAB]\n')
            SCRIPT.writelines('\n')
            SCRIPT.writelines('[COMMON]\n')
#            if("[Data8TeV_" in line) : SCRIPT.writelines('CMSSW.pset            = run_muonTPAnalyzer_data_cfg.py\n')
	    if("[Data8TeV_" in line) : SCRIPT.writelines('CMSSW.pset            = run_muonIsoTPAnalyzer_data_cfg.py\n')
	    if("[MC8TeV_" in line) :   SCRIPT.writelines('CMSSW.pset            = mc_cfg.py\n')
            SCRIPT.writelines('USER.user_remote_dir  = /store/user/rewang/Jan21_2014/\n')
	    SCRIPT.writelines('#submit_host      = cern_vocms83\n')
	    SCRIPT.writelines('#submit_host      = cern_vocms20\n')
	    SCRIPT.writelines('#submit_host      = unl_hcc-crabserver\n')
	    SCRIPT.writelines('#submit_host      = ucsd_submit-4\n')
	    SCRIPT.writelines('submit_host      = ucsd_submit-6\n')
	    if("[Data8TeV_" in line) : SCRIPT.writelines('CMSSW.lumi_mask       = Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt')
	    SCRIPT.writelines('\n\n\n\n')

	    #print line
	    lists.append(line)
	    SCRIPT.writelines(line)
	    nextline = fp.next()
	    #print nextline
	    SCRIPT.writelines(nextline+'\n')
	    SCRIPT.close()

	    #if "MC8TeV_ZH125" in line:
	    #   break
	    #os.system('multicrab -create')
	    #os.system('multicrab -create -submit')


#print lists
ALLSCRIPT.close()

#os.system('more script_completedjobs.sh')

