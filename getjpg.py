# # -*- coding: UTF-8 -*-
# from urllib import request
# import re
# def getHtml(url):
#     page = request.urlopen(url)
#     html = page.read().decode(encoding='utf-8',errors='strict')
#     return html
#
# def getjpg(html):
#      rs = r'src=(http.*?\.jpg)'
#      imgre = re.compile(rs)
#      jpg = re.findall(imgre,str(html))
#     # return jpg
#      x = 0
#      for imgurl in jpg:
#         request.urlretrieve(imgurl,'%s.jpg' % x)
#         x+=1
#
# # html = getHtml("https://image.baidu.com/")
# # lines = getjpg(html)
# # file = open('a','w')
# # file.write(str(lines))
# print(getHtml("https://image.baidu.com/"))

# -*- coding: utf-8 -*-
import urllib.request
import re
url='https://tieba.baidu.com/index.html?traceid='

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode(encoding='UTF-8',errors='strict')
    return html
def getjpg(html):
      rs = r'src="http.*?\.jpg"'
      imgre = re.compile(rs)
      jpg = re.findall(imgre,str(html))
      return jpg

h = getjpg(getHtml(url))
file = open('fa.py', 'w')
file.write(str(h))
#     return html
# print(getHtml(url))
