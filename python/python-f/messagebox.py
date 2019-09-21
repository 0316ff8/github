# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:46:46 2019

@author: User
"""

#Message Box

import tkinter as tk
import tkinter.messagebox as msg
base = tk.Tk()                                                                 #建立視窗
base.withdraw()                                                                #隱藏建立的視窗

response = msg.askyesno('糟糕!!!','還好嗎?')                                     #函式第一參數為視窗標題,第二參數為視窗內顯示文字,response若畫面選是為True,選否False

if(response==True):                                                            #判斷式若為True顯示'沒問題',False為'有問題'
    print('沒問題')
else:
    print('有問題')
base.mainloop()                                                                #讓GUI介面可以顯示出來