__author__ = 'oliveryiwang'

import urllib
import urllib2
from bs4 import BeautifulSoup
#import cookielib
import os
import sys
import re
import csv
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")

response = urllib2.urlopen('http://dblp1.uni-trier.de/pers/hd/r/Redmiles:David_F=')
html_src = response.read()

parser = BeautifulSoup(html_src)

publications = parser.findAll("ul", attrs = {'class': 'publ-list'})

#find the mappings between DOI and Title for journal paper

journalpub = parser.findAll('li', attrs = {'class': 'entry article'})

journalpaper = []

for item in journalpub:
    tempdoi = item.find('a', href=True)
    doi = tempdoi['href']
    temptitle = item.find('span', attrs = {'class': 'title'})
    title = temptitle.text
    journalpaper.append([doi, title])

#find the mappings between DOI and Title for conference paper

confpub = parser.findAll('li', attrs = {'class': 'entry inproceedings'})

confpaper = []

for item in confpub:
    tempdoi = item.find('a', href=True)
    doi = tempdoi['href']
    temptitle = item.find('span', attrs = {'class': 'title'})
    title = temptitle.text
    confpaper.append([doi, title])

#output to two csv file
try:
    os.stat('./output')
except:
    os.mkdir('./output')

with codecs.open('./output/journalpaper.csv', 'w', 'utf-8') as fout:
    fw = csv.writer(fout, delimiter = ',')
    fw.writerows(journalpaper)

with codecs.open('./output/confpaper.csv', 'w', 'utf-8') as fout:
    fw = csv.writer(fout, delimiter = ',')
    fw.writerows(confpaper)
