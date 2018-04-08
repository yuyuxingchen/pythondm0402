# -*- coding: utf-8 -*-
import urllib.request
import re
import os
url='https://tieba.baidu.com/index.html?traceid'

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode(encoding='UTF-8',errors='strict')
    return html

def getjpgurl(html):
    rs = r'src="(https://[A-Z0-9a-z\s\%\.\_\/-=]*?\.jpg)"'
    imgre = re.compile(rs,re.S)
    jpgurl = re.findall(imgre,html)
    return jpgurl

def getjpg(jpgurl):
    jpglist = []
    os.chdir('picture')
    x = 0
    for i in range(10):
        jpglist.append(jpgurl[i])
    for jpgurl in jpglist:
        urllib.request.urlretrieve(jpgurl, '%s.jpg' % x)
        x = x + 1

html = getHtml(url)
getjpgurl = getjpgurl(html)
getjpg(getjpgurl)



