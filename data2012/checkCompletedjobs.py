#!/usr/bin/env python
import os,sys
import getopt
import commands
import json

"""
Gets the value of a given item
(if not available a default value is returned)
"""
def getByLabel(desc,key,defaultVal=None) :
    try :
        return desc[key]
    except KeyError:
        return defaultVal



SCRIPT = open('script_completedjobs.sh',"w")
samplesDB = '/afs/cern.ch/work/r/rewang/HiggsZZd/HZZ/CMSSW_5_3_11/src/CMGTools/HiggsAna2l2v/data/dijet_sample.json'

#open the file which describes the sample
jsonFile = open(samplesDB,'r')
procList=json.load(jsonFile,encoding='utf-8').items()

asplit=1

status, output = commands.getstatusoutput('ls -d multicrab_*')
alljobs = output.split()
for ajob in alljobs:
    joblog = 'output_'+ajob+'.log'
    print 'running: '+joblog
    SCRIPT.writelines('\n###################' + '\n')
    SCRIPT.writelines('#' + joblog + '\n')
    SCRIPT.writelines('###################' + '\n\n')
    with open(joblog) as fp:

	myfinishjobs = '0'
    	for line in fp:

	  #if "Jobs with Wrapper Exit Code :" in line:
	  #    columns = line.split()
	  #    if columns[8] != "0" :
	  #  	SCRIPT.writelines('#' + line)
          #  	#print line
	  #  	nextline = fp.next()
	  #  	SCRIPT.writelines('#' + nextline + '\n')
	  #  	NLcolumns = nextline.split()
	  #  	#print NLcolumns[3]
	  #  	SCRIPT.writelines('multicrab -get '      + NLcolumns[3] + ' -c ' + ajob + ';\n')
	  #  	SCRIPT.writelines('multicrab -resubmit ' + NLcolumns[3] + ' -c ' + ajob + ';\n')

	  if "Log file" in line:
	      logfile = line.split()
	      llfile = logfile[3].split('/')
	      print llfile[16]

              for proc in procList :
                for desc in proc[1] :
                        data = desc['data']
                        #print data
                        for d in data :
                                origdtag = getByLabel(d,'dtag','')
                                split = getByLabel(d,'split','')
                                #print origdtag + ': ' + str(split)
                                if(llfile[16] == origdtag): asplit = split

              #print str(asplit)


	  if "Jobs with Wrapper Exit Code : 0" in line:
	      #print line
	      finishjobs = line.split()
	      myfinishjobs = finishjobs[1]
	      #print finishjobs[1]

	  if "Total Jobs" in line:
	       #print line
	       totaljobs = line.split()
	       #print totaljobs[1]
	  #    SCRIPT.writelines('#' + line + '\n')
	  #    SCRIPT.writelines('multicrab -submit  -c ' + ajob + ';\n')

	print "Finished Jobs: " + myfinishjobs + "  >>>>> Total jobs: " + totaljobs[1]
	if myfinishjobs == totaljobs[1]:
	  SCRIPT.writelines('# Total jobs: ' + totaljobs[1] + ' finished jobs: '+ finishjobs[1] + '\n')
	  SCRIPT.writelines('#' + ajob + '\n')
	  SCRIPT.writelines('multicrab -get -c ' + ajob + ';\n')
	  SCRIPT.writelines('multicrab -report -c ' + ajob + ';\n')
	  SCRIPT.writelines('#mkdir -p jsonFile;\n');
	  SCRIPT.writelines('#cp '+llfile[16]+'/res/task_missingLumiSummary.json jsonFile/'+llfile[16]+'_missingLumiSummary.json;\n')
	  SCRIPT.writelines('#cp '+llfile[16]+'/res/lumiSummary.json jsonFile/'+llfile[16]+'_lumiSummary.json;\n')
	  SCRIPT.writelines('#sh mergeOutput.sh ' + llfile[16] + ' '+ str(asplit) + ' ;\n')
	  SCRIPT.writelines('# multicrab -clean -c ' + ajob + ';\n')
	  SCRIPT.writelines('# rm -r ' + ajob + ';\n')
	  SCRIPT.writelines('# rm -r ' + llfile[16] + ';\n')


SCRIPT.close()

#os.system('more script_completedjobs.sh')

