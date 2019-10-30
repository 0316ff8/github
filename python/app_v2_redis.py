#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''

整體功能描述

'''


# In[2]:


'''

Application 主架構

'''

# 引用Web Server套件
from flask import Flask, request, abort

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

# 引用無效簽章錯誤
from linebot.exceptions import (
    InvalidSignatureError
)

# 載入json處理套件
import json

# 載入基礎設定檔
secretFileContentJson=json.load(open("./line_secret_key",'r'))
server_url=secretFileContentJson.get("server_url")

# 設定Server啟用細節
app = Flask(__name__,static_url_path = "/素材" , static_folder = "./素材/")

# 生成實體物件
line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))
handler = WebhookHandler(secretFileContentJson.get("secret_key"))

# 啟動server對外接口，使Line能丟消息進來
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# In[3]:


# Redis端設定
# 1.Redis防火牆關閉
# 2.Redis Server啟動時後面帶上 --protected-mode no
# src/redis-server  --protected-mode no

# 串接Redis需安裝套件
# !pip install redis
# import redis
# r = redis.Redis(host='192.168.48.132', port=6379)
# r.set('name', 'messi')
# print (r.get('name'))


# In[4]:


'''

消息判斷器

讀取指定的json檔案後，把json解析成不同格式的SendMessage

讀取檔案，
把內容轉換成json
將json轉換成消息
放回array中，並把array傳出。

'''

# 引用會用到的套件
from linebot.models import (
    ImagemapSendMessage,TextSendMessage,ImageSendMessage,LocationSendMessage,FlexSendMessage
)

from linebot.models.template import (
    ButtonsTemplate,CarouselTemplate,ConfirmTemplate,ImageCarouselTemplate
    
)

from linebot.models.template import *

def detect_json_array_to_new_message_array(fileName):
    
    #開啟檔案，轉成json
    with open(fileName) as f:
        jsonArray = json.load(f)
    
    # 解析json
    returnArray = []
    for jsonObject in jsonArray:

        # 讀取其用來判斷的元件
        message_type = jsonObject.get('type')
        
        # 轉換
        if message_type == 'text':
            returnArray.append(TextSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'imagemap':
            returnArray.append(ImagemapSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'template':
            returnArray.append(TemplateSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'image':
            returnArray.append(ImageSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'sticker':
            returnArray.append(StickerSendMessage.new_from_json_dict(jsonObject))  
        elif message_type == 'audio':
            returnArray.append(AudioSendMessage.new_from_json_dict(jsonObject))  
        elif message_type == 'location':
            returnArray.append(LocationSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'flex':
            returnArray.append(FlexSendMessage.new_from_json_dict(jsonObject))    

    # 回傳
    return returnArray


# In[5]:


'''

handler處理關注消息

用戶關注時，讀取 素材 -> 關注 -> reply.json

將其轉換成可寄發的消息，傳回給Line

'''

# 引用套件
from linebot.models import (
    FollowEvent
)

# 關注事件處理
@handler.add(FollowEvent)
def process_follow_event(event):
    
    # 讀取並轉換
    result_message_array =[]
    replyJsonPath = "素材/關注/reply.json"
    result_message_array = detect_json_array_to_new_message_array(replyJsonPath)

    # 呼叫個人用戶名，與用戶第一次接觸打招呼
    user_profile = line_bot_api.get_profile(event.source.user_id)
    hello = {
      "type": "text",
      "text": "您好!" + str(user_profile.display_name) + "\n歡迎您使用「RunningAI」"
    }
    result_message_array.insert(0, TextSendMessage.new_from_json_dict(hello))
    
        
    #綁定 rich_menu
    linkRichMenuId = open("素材/rich_menu_4/rich_menu_id", 'r').read()
    line_bot_api.link_rich_menu_to_user(event.source.user_id,linkRichMenuId)
    
    
    # 消息發送
    line_bot_api.reply_message(
        event.reply_token,
        result_message_array
    )

    
    # Redis端設定
    # 1.Redis防火牆關閉
    # 2.Redis Server啟動時後面帶上 --protected-mode no
    # src/redis-server  --protected-mode no

    # 串接Redis需安裝套件
    # !pip install redis
    import redis
    #r = redis.Redis(host='192.168.48.132', port=6379)
    r = redis.Redis(host='10.120.28.22', port=6379)
    myfile = json.dumps(vars(user_profile),sort_keys=True)
    print(myfile)
    print(type(myfile))
    r.set('messi', myfile)

        
    # r.set('name', 'messi')
    # print (r.get('name'))

    # 將用戶資訊存在檔案內
    # with open("users.txt", "a") as myfile:
    #    myfile.write(json.dumps(vars(user_profile),sort_keys=True))
    #    myfile.write('\r\n')
        
        
    
    
    #擷取tag訊息
    #dn = "ID_message/user_event.txt"
    #user_event = {}
    #with open(dn, "a") as myfile:
        #user_event["user_id"] = vars(user_profile)["user_id"]
        #user_event["tag"] = "user of first entering"
        #user_event["time"] = event.timestamp
        #user_event["product_ID"] = "now to choose"
        
        #myfile.write(json.dumps(user_event,sort_keys=True))
        #myfile.write('\r\n')


# In[6]:


'''

handler處理文字消息

收到用戶回應的文字消息，
按文字消息內容，往素材資料夾中，找尋以該內容命名的資料夾，讀取裡面的reply.json

轉譯json後，將消息回傳給用戶

'''

# 引用套件
from linebot.models import (
    MessageEvent, TextMessage
)

# 文字消息處理
@handler.add(MessageEvent,message=TextMessage)
def process_text_message(event):
    dict1 = {'路線推薦': '1-1', '活動賽事': '2-1', '開始運動': '3-1', '查看體能狀態': '4-1', '查詢我的歷史運動紀錄': '5-1', '查看詳細記錄': '5-2', '聯絡我們': '6-1'}
    # 讀取本地檔案，並轉譯成消息
    result_message_array =[]
    print(event.message.text)
    print(dict1.get(str(event.message.text)))
    replyJsonPath = "./素材/"+dict1.get(event.message.text)+".json"
    result_message_array = detect_json_array_to_new_message_array(replyJsonPath)

    # 發送
    line_bot_api.reply_message(
        event.reply_token,
        result_message_array
    )
    print('process_text_message done')


# In[7]:


'''

handler處理Postback Event

載入功能選單與啟動特殊功能

解析postback的data，並按照data欄位判斷處理

現有三個欄位
menu, folder, tag

若folder欄位有值，則
    讀取其reply.json，轉譯成消息，並發送

若menu欄位有值，則
    讀取其rich_menu_id，並取得用戶id，將用戶與選單綁定
    讀取其reply.json，轉譯成消息，並發送

'''
from linebot.models import (
    PostbackEvent
)

from urllib.parse import parse_qs 

@handler.add(PostbackEvent)
def process_postback_event(event):
    
    
    query_string_dict = parse_qs(event.postback.data)  # 將字串結果依照特定符號條件轉換成字典
#     print(event.postback.data)
#     print('query_string_dict',query_string_dict)
    if 'type' in query_string_dict:
        dict1 = {'walk': '2-2-walk', 'run': '2-2-run', 'ride': '2-2-ride'}
        result_message_array =[]
        print(query_string_dict.get('type'))
        replyJsonPath = './素材/'+dict1.get(query_string_dict.get('type')[0])+".json"
        print(replyJsonPath)
        result_message_array = detect_json_array_to_new_message_array(replyJsonPath)
  
        line_bot_api.reply_message(
            event.reply_token,
            result_message_array
        )
        print('process_postback_event done')
    elif 'type_locate' in query_string_dict:
    
        result_message_array =[]
        print(query_string_dict.get('type_locate'))
        replyJsonPath = './素材/2-3.json'
        result_message_array = detect_json_array_to_new_message_array(replyJsonPath)
#         print(result_message_array)
#         result_message_array[0]['template']['columns'][1]['actions'][1]['text'] = '騙你的'
#         result_message_array[0].template.columns[1].actions[1].label = '還是騙你的'
#         print(result_message_array[0].template.columns[1].actions[1].text)
#         print(result_message_array)
        line_bot_api.reply_message(
            event.reply_token,
            result_message_array
        )
        print('process_postback_event done')
    elif 'sport' in query_string_dict:
        dict1 = {'climb': '1-2-climb', 'run': '1-2-run'}
        result_message_array =[]
        print(query_string_dict.get('sport'))
        replyJsonPath = './素材/'+dict1.get(query_string_dict.get('sport')[0])+".json"
        result_message_array = detect_json_array_to_new_message_array(replyJsonPath)
#         print(result_message_array)
#         result_message_array[0]['template']['columns'][1]['actions'][1]['text'] = '騙你的'
#         result_message_array[0].template.columns[1].actions[1].label = '還是騙你的'
#         print(result_message_array[0].template.columns[1].actions[1].text)
#         print(result_message_array)
        line_bot_api.reply_message(
            event.reply_token,
            result_message_array 
        )
        print('process_postback_event done')
    elif 'sport_locate' in query_string_dict:
        dict1 = {'run:PD': '1-3-run-PD', 'run:KS': '1-3-run-KS','run:TC': '1-3-run-TC', 
                 'climb:PD': '1-3-climb-PD', 'climb:KS': '1-3-climb-KS','climb:TC': '1-3-climb-TC', }
        result_message_array =[]
        print(query_string_dict.get('sport_locate'))
        replyJsonPath = './素材/'+dict1.get(query_string_dict.get('sport_locate')[0])+".json"
        print(replyJsonPath)
        result_message_array = detect_json_array_to_new_message_array(replyJsonPath)
#         print(result_message_array)
#         result_message_array[0]['template']['columns'][1]['actions'][1]['text'] = '騙你的'
#         result_message_array[0].template.columns[1].actions[1].label = '還是騙你的'
#         print(result_message_array[0].template.columns[1].actions[1].text)
#         print(result_message_array)
        line_bot_api.reply_message(
            event.reply_token,
            result_message_array
        )
        print('process_postback_event done')
    elif 'sport3' in query_string_dict:
        dict1 = {'walk': '3-2', 'run': '3-2'}
        result_message_array =[]
        print(query_string_dict.get('sport3'))
        replyJsonPath = './素材/'+dict1.get(query_string_dict.get('sport3')[0])+".json"
        result_message_array = detect_json_array_to_new_message_array(replyJsonPath)
#         print(result_message_array)
#         result_message_array[0]['template']['columns'][1]['actions'][1]['text'] = '騙你的'
#         result_message_array[0].template.columns[1].actions[1].label = '還是騙你的'
#         print(result_message_array[0].template.columns[1].actions[1].text)
#         print(result_message_array)
        line_bot_api.reply_message(
            event.reply_token,
            result_message_array 
        )
        print('process_postback_event done')
    elif 'sporting' in query_string_dict:
        dict1 = {'start': '3-3', 'stop': '3-4'}
        result_message_array =[]
        print(query_string_dict.get('sporting'))
        replyJsonPath = './素材/'+dict1.get(query_string_dict.get('sporting')[0])+".json"
        result_message_array = detect_json_array_to_new_message_array(replyJsonPath)
#         print(result_message_array)
#         result_message_array[0]['template']['columns'][1]['actions'][1]['text'] = '騙你的'
#         result_message_array[0].template.columns[1].actions[1].label = '還是騙你的'
#         print(result_message_array[0].template.columns[1].actions[1].text)
#         print(result_message_array)
        line_bot_api.reply_message(
            event.reply_token,
            result_message_array 
        )
        print('process_postback_event done')


# In[ ]:


'''

Application 運行（開發版）

'''
if __name__ == "__main__":
    app.run(host='0.0.0.0')


# In[ ]:


'''

Application 運行（heroku版）

# import os
# if __name__ == "__main__":
#     app.run(host='0.0.0.0',port=os.environ['PORT'])

'''


# In[ ]:




