#!/usr/bin/env python
import os,sys
import getopt
import commands
CopyRights  = '\033[92m'
CopyRights += '####################################\n'
CopyRights += '#     checkDuplicates.py Script    #\n'
CopyRights += '#           Ren-Jie Wang           #\n'
CopyRights += '#       renjie.wang@cern.ch        #\n'
CopyRights += '#             Sep 2014             #\n'
CopyRights += '####################################\n'
CopyRights += '\033[0m'


dir='-1'
#nsplit='-1'
print CopyRights

def help() :
   print '  -c --> gives a directory'
   #print '  -n --> # of split files'

#parse the options
try:
   # retrive command line options
   shortopts  = "c:n:?"
   opts, args = getopt.getopt( sys.argv[1:], shortopts )
except getopt.GetoptError:
   # print help information and exit:
   print "ERROR: unknown options in argument %s" % sys.argv[1:]
   help()
   sys.exit(1)

for o,a in opts:
   if o in("-?", "-h"):
      help()
      sys.exit(1)
   elif o in('-c'): dir = a
   #elif o in('-n'): nsplit = a


if(dir == '-1'):# or nsplit=='-1'):
   help()
   sys.exit(1)


AllList='FileList_'+dir+'.txt'
tofile = open(AllList,"w")
count=0
status, allFiles = commands.getstatusoutput('ls ' + dir + '/res/analysis_*.root | grep root ')
for line in allFiles.split():
        count = count+1
print 'Total Files: '+str(count)#+' nsplit: '+nsplit

DOUBLE_CNT = open('script_double_count.sh',"w")

for i in range(count):
	status, allFiles = commands.getstatusoutput('ls ' + dir + '/res/analysis_'+str(i+1)+'_*.root | grep root ')
	counted='-1'
	for line in allFiles.split():
		#print line
		if counted=='-1': tofile.writelines(line+', #FILE'+str(i+1)+'_'+'\n')
	        else:	 	  
			#print 'has countted: '+str(i+1)
			print line
			DOUBLE_CNT.writelines('rm '+line+';\n')
			
		counted='1'
tofile.close()
DOUBLE_CNT.close()




