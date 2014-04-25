#!/usr/bin/env python
import os,sys
import getopt
import commands

SCRIPT = open('script_jobstatus.sh',"w")

#os.system('for ifile in $(ls -d multicrab_*); do echo ${ifile}; done')
status, output = commands.getstatusoutput('ls -d multicrab_*')
alljobs = output.split()
#print alljobs
#print len(alljobs)
SCRIPT.writelines('#!bin/sh\n\n')
SCRIPT.writelines('rm output_*.log\n\n')
for ajob in alljobs:
	print ajob
	SCRIPT.writelines('multicrab -status -c ' + ajob + ' >& output_'+ajob+'.log &'+'\n')


SCRIPT.close()
#os.system('source script_jobstatus.sh')

