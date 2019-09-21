# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:45:27 2019

@author: User
"""

import requests
from bs4 import BeautifulSoup
yahoo_sport_xml = requests.get('https://tw.news.yahoo.com/rss/sports')
soup = BeautifulSoup(yahoo_sport_xml.text,"html.parser")
#print(type(soup))
#print(soup.findAll('item'))
for news in soup.find_all('item'):
    print(news.title.string)                  #.string為只顯示字串