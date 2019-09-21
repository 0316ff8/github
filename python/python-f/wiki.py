# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:02:36 2019

@author: User
"""


#以json格式取資料顯示出來
import requests,pprint
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'json','action':'query','titles':'鋼鐵人','prop':'revisions','rvprop':'content'}
wiki_data = requests.get(api_url,params=api_params).json()
pprint.pprint(wiki_data)



#將資料取出寫入到html檔案中
import requests,codecs
api_base_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm','action':'query','titles':'鋼鐵人','prop':'revisions','rvprop':'content'}
wiki_data = requests.get(api_base_url,params=api_params)
fo = codecs.open('C:\\Users\\User\\Desktop\\wiki.html','w','utf-8')
fo.write(wiki_data.text)
fo.close()