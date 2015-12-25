#!bin/csh
python checkstatus.py ; python checkFailjobs.py ; sh script_submitjobs.sh ; python checkstatus.py ; python checkSubmitjobs.py ;

