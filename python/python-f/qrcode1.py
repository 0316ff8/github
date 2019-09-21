# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:22:29 2019

@author: User
"""

import qrcode                                                                  #匯入qrcode模組
encode_text = '高雄發大財'                                              #將字串放入變數之中
img = qrcode.make(encode_text)                                                 #將字串傳入qrcode模組的make方法就能建立圖片
#print(type(img))                                                              #檢查一下型態
img.show()                                                                     #開啟qrcode圖片