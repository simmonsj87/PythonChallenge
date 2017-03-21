# level1.py
# http://www.pythonchallenge.com/pc/def/map.html
# the hint is the decode a string by shifting all the characters by 2, wrapping around to the beginning.  Be sure to ignore none a-zA-Z characters

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newStr = ""
newChar = ''
newOrd = 0
for char in str:
	# find ordinal number of character
	newOrd = ord(char)
	#only shift if a-z
	if(97 <= ord(char) <= 122):
		newOrd = ord(char)+2
		# wrap around
		if newOrd > 122:
			newOrd = newOrd - 26
	
	newStr = newStr + chr(newOrd)

print newStr

str = "map"
newStr = ""
newChar = ''
newOrd = 0
for char in str:
	newOrd = ord(char)
	if(97 <= ord(char) <= 122):
		newOrd = ord(char)+2
		if newOrd > 122:
			newOrd = newOrd - 26
	
	newStr = newStr + chr(newOrd)

print newStr

print "http://www.pythonchallenge.com/pc/def/ocr.html"
