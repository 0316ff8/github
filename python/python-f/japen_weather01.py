# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:43:21 2019

@author: User

日本天氣抓取練習
"""

#import requests
#api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
#payload = {'city':'130010'}
#weather_data = requests.get(api_url,params=payload).json()
#print(weather_data['forecasts'][0]['dateLabel'] + '的天氣是:' +
#      weather_data['forecasts'][0]['telop'])
#print(weather_data['forecasts'][1]['dateLabel'] + '的天氣是:' +
#      weather_data['forecasts'][1]['telop'])


#改用迴圈方式
import requests
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url,params=payload).json()
for weather in weather_data['forecasts']:
    print(weather['dateLabel'] + '的天氣是:' + weather['telop'])