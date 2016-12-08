#!/usr/bin/python2
#find  /path/to/dest -type f -empty -delete
import os
import sys
def killall(a='.lock'):
	line='find . -name "'+'*'+a+'" -type f -delete'
	os.system(line)
def null_arg():
	if len(sys.argv)==1 :
		return 1
	else :
		return 0
def select():
	c=1
	if null_arg()==0 :
		 for i in range(len(sys.argv)):
			if i==0:
				continue
			if "--help"==sys.argv[i]:
				print "Help Called"
				c=0
				break
			if "-h"==sys.argv[i]:
				print "Help 2 called"
				c=0
				break
			if "--fix-empty"==sys.argv[i]:
				print "Fix Empty"
				c=0
			if "--fix-lock"==sys.argv[i]:
				print "Fix lock"
				c=0
			if "--sync-all"==sys.argv[i]:
				print "Sync all"
				c=0
			if "--uninstall"==sys.argv[i]:
				print "Bye.. Please tell me what was wrong in the github repo."
				os.system("rm -rf /usr/bin/"+__file__[2:])
	else :
		print "This program requires a argument, please refer "+__file__+" -h for details. Argument oder matters."
 		c=0
	if c==1 :
		print "Argument Error!. Please reffer "+__file__+" -h for more details. Argument order matters."
select()
#print "Done!"
