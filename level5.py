#level5.py
# http://www.pythonchallenge.com/pc/def/peak.html

import urllib
import pickle

pickleFile = pickle.load(open(("banner.p"), "rb"))

print '\n'.join(["".join([p[0]*p[1] for p in row]) for row in pickleFile])

# http://www.pythonchallenge.com/pc/def/channel.html
