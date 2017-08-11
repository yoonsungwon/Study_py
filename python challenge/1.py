# -*- encoding:utf8 -*-
# http://www.pythonchallenge.com/pc/def/map.html
# http://www.pythonchallenge.com/pc/def/ocr.html
# http://wiki.pythonchallenge.com/index.php?title=Level1:Main_Page

import string
trans = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab'
 input='''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw
fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq
pcamkkclbcb. lmu ynnjw ml rfc spj.'''
print(input.translate(trans))

print('map'.translate(trans))