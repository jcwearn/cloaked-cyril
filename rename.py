#!/usr/bin/python
# author: Jackson Wearn
# description: a small script to rename the files in a directory
# initial idea from: http://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory

import os, sys, re

# lists to contain all the files and directories from root directory
filelist = []
dirlist = []

# counter that increments everytime a file or directory is renamed
count = 0
args = sys.argv # ['./rename.py', 'user_path/']

if not len(args) == 2: # program exits if there is not exaclly one argument
    print "Input Error. Usage: rename.py <path>"
    exit(1)

path = str(args[1:]) # returns string version of ['user_path/']
path = path[2:len(path)-2] # strips [' and '] from user_path/

#files = os.listdir(path) # returns a directory list of given user_path/

if path == '.':
    path = '';

# check if path contains Movie or TV so that the correct updates can be made to the file names
if "Movies/" in path:
    isMovie = True
elif "TV/" in path:
    isMovie = False

# get all files, directories, and subdirectories from the given path
# append files to filelist
# append directories and subdirectories to dirlist
for root, dirs, files in os.walk(path):
    for name in files:
	filelist.append(os.path.join(root, name))
    for name in dirs:
	dirlist.append(os.path.join(root, name))
    
# prints out all files contained in root directory and it's subdirectories
# used for testing (to be removed from final code)
print "Files"
for f in filelist:
    print f

# prints out all subdirectories contained in root directory and it's subdirectories
# used for testing (to be removed from final code)
print "\n"
print "Directories"
for d in dirlist:
    print d

# remove files that aren't of the following formats: avi, mkv, mp4, srt, zip
print "\n"
print "The following files will be deleted"
for file in filelist:
    if not (file.endswith('.avi') or file.endswith('.mkv') or file.endswith('.mp4') or file.endswith('.srt') or file.endswith('.zip')):
	print "--- " + file
	# uncomment below line when script is finished
	#os.remove(file)

    '''
    for f in files: # loop through directory list (files)
	# check that file doesn't begin with '.' and ends with 'avi','.mp4','.mkv','.srt' 
	if not f.startswith('.') and (f.endswith('.avi') or f.endswith('.mp4') or f.endswith('.mkv') or f.endswith('.srt')):
	    # check that file doesn't already follow the correct format [s[0-9]e[0-9]]
	    if not re.search('s[0-9]?[0-9]e[0-9]?[0-9]',f, re.IGNORECASE):
		# index of first digit of 3 digit number (e.g. rome.hdtv.101.avi  : '101')
		idx_re = re.search('[0-9]?[0-9][0-9]',f).start() # this number determines what season the episode is in
		replacement = f[0:idx_re] + 's0' + f[idx_re] + 'e' + f[idx_re+1:]  # piece string together with correct format
		#os.rename(path + f, path + replacement) # replace the original with the new file name
		count = count + 1 # increment to track how many files are updated
     '''

print 'Finished: ' + str(count) + " file(s) updated"

'''
for root, dirs, files in os.walk(path):
    for name in files:
        print("File: " + os.path.join(root, name))
    for name in dirs:
        print("Directory: " + os.path.join(root, name))
'''
