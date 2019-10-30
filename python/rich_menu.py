#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
迴圈讀取本地列表，
    上傳設定檔，取得id，並將id寫入檔案中，而後上傳圖片

'''

import json
from linebot import LineBotApi

# 載入安全設定檔
secretFileContentJson=json.load(open("./line_secret_key",'r'))
line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))



'''
rich_menu的本地列表
'''
rich_menu_array=['rich_menu_0','rich_menu_1','rich_menu_2','rich_menu_3','rich_menu_4']

from linebot.models import RichMenu

for rich_menu_name in rich_menu_array:

    
    # 創建菜單，取得menuId
    lineRichMenuId = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(json.load(open("素材/"+rich_menu_name+'/rich_menu.json','r'))))
    print("-設定檔上傳結果")
    print(lineRichMenuId)
    print(rich_menu_name)
    
                                           
    # id寫入本地端                              
    f = open("素材/"+rich_menu_name+"/rich_menu_id", "w")
    f.write(lineRichMenuId)
    f.close()                                       
 

    # 上傳照片至該id
    set_image_response=''
    with open("素材/"+rich_menu_name+'/rich_menu.jpg', 'rb') as f:
        set_image_response=line_bot_api.set_rich_menu_image(lineRichMenuId, 'image/jpeg', f)
        
    print("-圖片上傳結果")                                               
    print(set_image_response)
                                                                 


# In[2]:


'''

查詢帳號內擁有的richmenu 

'''

from linebot import (
    LineBotApi
)

import json

secretFileContentJson=json.load(open("./line_secret_key",'r'))
line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))

line_bot_api.get_rich_menu_list()


# In[3]:


'''

移除帳號內的richmenu

'''

from linebot import (
    LineBotApi
)

import json
secretFileContentJson=json.load(open("./line_secret_key",'r'))
line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))

# 設定要移除的rich_menu
rich_menu_name_array = ["rich_menu_0"]

for rich_menu_name in rich_menu_name_array:
    
    # 讀取rich_menu_id檔案，並告知 Line 進行刪除，並在刪除後，把本地檔案內容清除
    with open("素材/"+rich_menu_name+'/rich_menu_id', 'r') as myfile:
        rich_menu_id = myfile.read()
        deleteResult = line_bot_api.delete_rich_menu(rich_menu_id)
        print(deleteResult)
        
    f = open("素材/"+rich_menu_name+"/rich_menu_id", "w")
    f.write('')
    f.close() 


# In[4]:


'''

解除用戶綁定

'''

from linebot import (
    LineBotApi
)

import json

# rich_menu_id_array = ["rich_menu_0"]

secretFileContentJson=json.load(open("./line_secret_key",'r'))
line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))

self_user_id='U522e970618d9f07bcccdd649f6dd977f'
line_bot_api.unlink_rich_menu_from_user(self_user_id)


# In[5]:


'''

綁定個人用戶進行測試

'''

from linebot import (
    LineBotApi
)

import json

# rich_menu_id_array = ["rich_menu_0"]

secretFileContentJson=json.load(open("./line_secret_key",'r'))
line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))

self_user_id='U522e970618d9f07bcccdd649f6dd977f'
rich_menu_id='richmenu-df0c71f16113f13db92bee26f85c9219'

line_bot_api.unlink_rich_menu_from_user(self_user_id)
line_bot_api.link_rich_menu_to_user(self_user_id,rich_menu_id)


# In[ ]:




