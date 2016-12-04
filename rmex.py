#!/usr/bin/python3
import os
a=input("Enter the filetype (eg *.lock):")
line='find . -name "'+a+'" -type f -delete'
os.system(line)
print("Done!")
