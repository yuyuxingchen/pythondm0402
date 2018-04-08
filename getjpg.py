# -*- coding: utf-8 -*-
import urllib.request
import re
url='https://tieba.baidu.com/index.html?traceid'

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode(encoding='UTF-8',errors='strict')
    return html

def getjpg(html):
    rs = r'src="(https://[A-Z0-9a-z\s\%\.\_\/-=]*?\.jpg)"'
    imgre = re.compile(rs, flags=0)
    jpg = re.findall(imgre,html)
    return jpg
def jpg_to_a(jpg):
 #    with open('a', 'w+', encoding='utf-8', errors='strict') as f:
        text = []
        for i in range(20):
            comment=jpg[i]
            text.append(comment)
            #f.write(str(text))
        print(text)
html = getHtml(url)
jpg = getjpg(html)
jpg_to_a(jpg)


