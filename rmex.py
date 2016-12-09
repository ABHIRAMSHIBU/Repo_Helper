#!/usr/bin/python2
import os
import sys
repo_error="Repo is not initialized in this directory. Please check PWD."
root_error="You does not appear to be root, use sudo or su to be root."
permission_error="If any permission error occurs, please be root or contact your administrator."
def empty_fix():
	line='find . -type f -empty -delete'
	os.system(line)
def root_check():
	a=os.popen("whoami").read()
	if "root" in a :
		return 1
	else :
		return 0
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
				print "Normal usage "+__file__+" --fix-empty --fix-lock --sync-all"
				print "-h or --help displays this message"
				print "--fix-empty  deletes all empty files (Corrupt)"
				print "--fix-lock deletes all .lock files (Git crash)"
				print "--uninstall  unintstalla itself from system dir if exists in same name"
				print "--install installs into the system"
				print "Licensed under Open GPL 2.0"
				c=0
				break
			if "-h"==sys.argv[i]:
				print "Script coded by Abhiram Shibu, contact abhiramshibu1998@gmail.com"
				print "Normal usage "+__file__+" --fix-empty --fix-lock --sync-all"
				print "-h or --help displays this message"
				print "--fix-empty  deletes all empty files (Corrupt)"
				print "--fix-lock deletes all .lock files (Git crash)"
				print "--uninstall  unintstalla itself from system dir if exists in same name"
				print "--install installs itself into system"
				print "Licensed under Open GPL 2.0"
				c=0
				break
			if "--fix-empty"==sys.argv[i]:
				empty_fix()
				print 'Fixed empty!'
				print permission_error
				c=0
			if "--fix-lock"==sys.argv[i]:
				killall()
				print 'Fixed lock!'
				print permission_error
				c=0
			if "--sync-all"==sys.argv[i]:
				os.system("repo sync -c --force-sync --force-broken --no-tags --no-clone-bundle -f")
				c=0
			if "--uninstall"==sys.argv[i]:
				if root_check()==1 :
					print "Bye.. Please tell me what was wrong in the github repo."
					os.system("rm -rf /usr/bin/"+__file__[2:])
				else :
					print root_error
			if "--install"==sys.argv[i]:
				if root_check()==1:
					print "Installing to system!"
					os.system("cp "+__file__+" /usr/bin/")
				else :
					print root_error
	else :
		print "This program requires a argument, please refer "+__file__+" -h for details. Argument oder matters."
 		c=0
	if c==1 :
		print "Argument Error!. Please reffer "+__file__+" -h for more details. Argument order matters."
if (os.path.exists(".repo")):
	select()
else:
	print repo_error
#print "Done!"
