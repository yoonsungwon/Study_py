# -*- encoding:utf8 -*-
# http://www.pythonchallenge.com/pc/def/peak.html
# http://www.pythonchallenge.com/pc/def/peak.php
# http://wiki.pythonchallenge.com/index.php?title=Level4:Main_Page
from email.mime import audio

import sys
import pickle
import urllib

handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)

for elt in data:
    print "".join([e[1] * e[0] for e in elt])