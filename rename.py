#!/usr/bin/python
# author: Jackson Wearn
# description: a small script to rename the files in a directory
# snippets taken from: http://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory

import os
import sys
import re

args = sys.argv

if not len(args) == 2:
    print "Input Error. Usage: rename.py <path>"
    exit(1)

path = str(args[1:])
path = path[2:len(path)-2]
print path

files = os.listdir(path) 

for f in files:
    if not f.startswith('.') and (f.endswith('.avi') or f.endswith('.mp4') or f.endswith('.mkv') or f.endswith('.srt')):
	if not re.search('s[0-9]?[0-9]e[0-9]?[0-9]',f, re.IGNORECASE):
	    
	    replacement = f[0:5] + 's01e' + f[6:]  
	    print "orig: " + f
	    print "replacement: " + replacement
	    #os.rename(f, replacement)

