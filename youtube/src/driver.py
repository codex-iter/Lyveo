""" Lyveo - Youtube Link to Video Maker
	- Fetch the subtitles of the video

"""

# Importing Libraries
import os
import subprocess as sp

# Prompt user for the youtube link
url = input('Youtube Link: ')

# Fetch the subtitles
query = 'dl-youtube-cc ' + url + ' > tempfile'
os.system(query)

# Get the contents stored to the file
# Scraping the last word which contains the file name
query = "awk 'END {print $NF}' tempfile"
tempfilename = sp.check_output(query, shell=True)

# Cleaning the file name
temp = [chr(char) for char in tempfilename]
temp.pop(-1)
filename = ''.join(map(str, temp))
os.system('rm tempfile')
