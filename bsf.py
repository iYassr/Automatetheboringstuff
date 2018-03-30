from builtins import print

import requests, bs4
file = open('example.html','r')
noStrachSoup = bs4.BeautifulSoup(file.read(),'lxml')
print(type(noStrachSoup))
print(type(noStrachSoup.select('p')))
listofp = noStrachSoup.select('p')
print(listofp[0].getText())
print(listofp[0].attrs)

