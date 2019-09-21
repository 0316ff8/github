#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
r = requests.get('http://tw.yahoo.com')
print(r.text)


# In[3]:


import requests
import pprint
r = requests.get('http://tw.yahoo.com')
pprint.pprint(r.text)


# In[4]:


import requests
import pprint
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
weather_data = requests.get(api_url).json()
pprint.pprint(weather_data)


# In[7]:


url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(url,params=payload).json()
pprint.pprint(weather_data)


# In[9]:


weather_data.keys()


# In[10]:


pprint.pprint(weather_data['forecasts'][0])


# In[ ]:




