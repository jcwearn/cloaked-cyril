# author: Jackson Wearn
# description: a small script to rename the files in a directory
# snippets taken from: http://stackoverflow.com/questions/225735/batch-renaming-of-files-in-a-directory


import os

files = os.listdir('.') 

for f in files:
    if not f.startswith('.') and not f == 'rename.py' and not f == 'rename.py~':
	replacement = f[0:5] + 's01e' + f[6:]  
	os.rename(f, replacement)
