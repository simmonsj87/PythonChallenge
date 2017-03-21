#level2.py
# "http://www.pythonchallenge.com/pc/def/ocr.html"
import urllib
import re

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

html = urllib.urlopen(url).read()
comments = re.findall('<!--.*?-->',html, re.DOTALL)
rareChars = comments[1]

myDict = {}

for char in rareChars:
	# myDict[char] = myDict.get(char,0) + 1
	if(myDict.has_key(char)):
		myDict[char] = myDict[char] + 1
	else:
		myDict[char] = 1

newStr = ""
for key, value in myDict.items():
	print key, '::', myDict[key]
	if(myDict[key] < 10):
		newStr = newStr + key
		
print newStr

print 'http://www.pythonchallenge.com/pc/def/equality.html'

