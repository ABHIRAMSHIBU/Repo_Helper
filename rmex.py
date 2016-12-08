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
				print "Script coded by Abhiram Shibu, contact abhiramshibu1998@gmail.com"
				print "Normal usage "+__file__" --fix-empty --fix-lock --sync-all"
				print "-h or --help displays this message"
				print "--fix-empty  deletes all empty files (Corrupt)"
				print "--fix-lock deletes all .lock files (Git crash)"
				print "--uninstall  unintstalla itself from system dir if exists in same name"
				print "Licensed under Open GPL 2.0"
				c=0
				break
			if "-h"==sys.argv[i]:
				print "Script coded by Abhiram Shibu, contact abhiramshibu1998@gmail.com"
				print "Normal usage "+__file__" --fix-empty --fix-lock --sync-all"
				print "-h or --help displays this message"
				print "--fix-empty  deletes all empty files (Corrupt)"
				print "--fix-lock deletes all .lock files (Git crash)"
				print "--uninstall  unintstalla itself from system dir if exists in same name"
				print "Licensed under Open GPL 2.0"
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
