# -*- coding: utf-8 -*-
import urllib.request
import re
import os


url='https://tieba.baidu.com/index.html?traceid'
dirname = 'picture'
res = r'src="(https://[A-Z0-9a-z\s\%\.\_\/-=]*?\.jpg)"'

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode(encoding='UTF-8',errors='strict')
    return html


def getJpgurl(html):
    rs = res
    imgre = re.compile(rs,re.S)
    jpgurl = re.findall(imgre,html)
    return jpgurl


def getJpg(jpgurl):
    jpglist = []
    if os.path.exists(dirname):
        os.chdir(dirname)
    else:
        os.mkdir(dirname)
        os.chdir(dirname)
        x = 0
        for i in range(20):
            jpglist.append(jpgurl[i])
        for jpgurl in jpglist:
            if os.path.isfile('%s.jpg'):
                pass
            else:
                urllib.request.urlretrieve(jpgurl, '%s.jpg' % x)
            x = x + 1


if __name__ == '__main__':
    html = getHtml(url)
    getjpgurl = getJpgurl(html)
    getJpg(getjpgurl)



