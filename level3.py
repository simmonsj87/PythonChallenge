#level3.py
# 'http://www.pythonchallenge.com/pc/def/equality.html'
import urllib
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

html = urllib.urlopen(url).read()
comments = re.findall('<!--.*?-->',html, re.DOTALL)
small = re.findall('[^A-Z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][^A-Z]', comments[0])

newStr = ''
for string in small:
	newStr = newStr + string[4]
	
print newStr
print 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
