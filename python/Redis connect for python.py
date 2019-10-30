#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Redis端設定
# 1.Redis防火牆關閉
# 2.Redis Server啟動時後面帶上 --protected-mode no
# src/redis-server  --protected-mode no

# 串接Redis需安裝套件
# !pip install redis
import redis
r = redis.Redis(host='192.168.48.132', port=6379)
r.set('name', 'messi')
print (r.get('name'))


# In[ ]:




