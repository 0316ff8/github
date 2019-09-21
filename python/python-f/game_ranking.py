# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:46:01 2019

@author: User
"""
import requests
from bs4 import BeautifulSoup
game_ranking_html = requests.get('https://acg.gamer.com.tw/billboard.php?t=2&p=Android')
game_ranking_html.encoding = 'UTF-8'
soup = BeautifulSoup(game_ranking_html.text,"html.parser")
#print(soup.find(class_='ACG-mainbox1').find(class_='ACG-maintitle').find('a').string)
for game in soup.find_all(class_='ACG-mainbox1'):
    print(game.find(class_='ACG-mainumber').string + ' ' + game.find(class_='ACG-maintitle').find('a').string
           + ' ' + game.find(class_='ACG-mainbox2').find('li').string)