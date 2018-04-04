#-*- coding: utf-8 -*-
import re
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
# def getImg(html):
#     reg = r'"src=".+ \.png "width"'
#     imgre = re.compile(reg)
#     imgrelist = re._pattern_type(imgre,html)
print(getHtml("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%A3%8E%E6%99%AF"))