#level4.py
# 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

import urllib
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothingValue = '12345'

while nothingValue:
	# added the divide by 2 (str to int and back to str)
	# hint given on one of the pages after initial run
	if nothingValue == '16044':
		nothingValue = str(16044/2)
	html = urllib.urlopen(url+nothingValue).read()
	print 'html ::', html;
	results = re.search('next nothing is (\d+)',html)
	print 'nothingValue :: ',nothingValue
	nothingValue = results.group(1)

print 'http://www.pythonchallenge.com/pc/def/peak.html'



