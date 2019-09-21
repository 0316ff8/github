# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:23:13 2019

@author: User
"""



import tkinter as tk                                                           #匯入tkinter模組別名tk
base = tk.Tk()                                                                 #透過tkinter將TK類別實體化
def supermode():                                                               #自訂supermode函式
    print('super mode!')                                                       #顯示字串super mode!
    
menubar = tk.Menu(base)                                                        #主要作為選單項目放置的場所 
filemenu = tk.Menu(menubar)                                                    #以選單列為基礎製作檔案選單
filemenu.add_command(label='supermode',command=supermode)                      #用add_command方法新增選單列可點擊的項目,將label設定字串為supermode,command設定點擊後執行supermode函式
menubar.add_cascade(label='Operation',menu=filemenu)                           #用add_cascade方法將filemenu與menubar建立關聯
base.config(menu=menubar)                                                      #將menubar配置在作為base的menu上
base.mainloop()                                                                #讓GUI介面可以顯示出來