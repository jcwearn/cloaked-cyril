# author: Jackson Wearn
# description: a small script to rename the files in a directory
# snippets taken from: http://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory


import os

files = os.listdir('.') 
for f in files:
    if not f.startswith('.'):
	print f
