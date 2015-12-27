#!/usr/bin/env python
import os,sys
import getopt
import commands

SCRIPT = open('script_submitjobs.sh',"w")

status, output = commands.getstatusoutput('ls -d multicrab_*')
alljobs = output.split()
for ajob in alljobs:
    joblog = 'output_'+ajob+'.log'
    print 'running: '+joblog
    SCRIPT.writelines('\n###################' + '\n')
    SCRIPT.writelines('#' + joblog + '\n')
    SCRIPT.writelines('###################' + '\n\n')
    with open(joblog) as fp:

    	for line in fp:

 	  if "Jobs Running" in line:
	      #print line

              #print line
              nline = fp.next()
              print nline
              #print nnline
              nncolumns = nline.split(':')[1].split()[0]
              SCRIPT.writelines('\n #' + nline)
              SCRIPT.writelines('multicrab -forceResubmit ' + nncolumns + ' -c ' + ajob + ';\n')

SCRIPT.close()

#os.system('more script_submitjobs.sh')

