from re import *


logs='''
46.4.66.76 - - [17/May/2015:08:05:02 +0000] "GET /downloads/product_1 HTTP/1.1" 200 0 "-" "Debian APT-HTTP/1.3 (1.0.1ubuntu2)"
62.75.198.179 - - [17/May/2015:08:05:06 +0000] "GET /downloads/product_2 HTTP/1.1" 302 490 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
'''

for i in finditer("200",logs):
    loctuple=i.span()
    print(loctuple)