#!/usr/bin/python
# author: Jackson Wearn
# description: a small script to rename the files in a directory
# initial idea from: http://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory

import os, sys, re

count = 0
args = sys.argv # ['./rename.py', 'user_path/']

if not len(args) == 2: # program exits if there is not exaclly one argument
    print "Input Error. Usage: rename.py <path>"
    exit(1)

path = str(args[1:]) # returns string version of ['user_path/']
path = path[2:len(path)-2] # strips [' and '] from user_path/

files = os.listdir(path) # returns a directory list of given user_path/

if path == '.':
    path = '';

for f in files: # loop through directory list (files)
    # check that file doesn't begin with '.' and ends with 'avi','.mp4','.mkv','.srt' 
    if not f.startswith('.') and (f.endswith('.avi') or f.endswith('.mp4') or f.endswith('.mkv') or f.endswith('.srt')):
	# check that file doesn't already follow the correct format [s[0-9]e[0-9]]
	if not re.search('s[0-9]?[0-9]e[0-9]?[0-9]',f, re.IGNORECASE):
	    # index of first digit of 3 digit number (e.g. rome.hdtv.101.avi  : '101')
	    idx_re = re.search('[0-9]?[0-9][0-9]',f).start() # this number determines what season the episode is in
	    replacement = f[0:idx_re] + 's0' + f[idx_re] + 'e' + f[idx_re+1:]  # piece string together with correct format
	    os.rename(path + f, path + replacement) # replace the original with the new file name
	    count = count + 1 # increment to track how many files are updated

print 'Finished: ' + str(count) + " file(s) updated"
