from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
# import lxml

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
# lx = BeautifulSoup(html.read(), 'lxml')
bs = BeautifulSoup(html.read(), 'html5lib')
print(bs.h1)
# print(lx.body)


