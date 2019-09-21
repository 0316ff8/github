# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:18:20 2019

@author: User
"""

import tkinter as tk                                                           #匯入tkinter模組別名tk
import tkinter.filedialog as fd                                                #匯入tkinter.filedialog模組別名fd
base = tk.Tk()                                                                 #透過tkinter將TK類別實體化
def open():                                                                    #自訂函式open
    filename = fd.askopenfilename()                                            #askopenfilename方法會顯示選擇的檔案視窗,選擇檔案後取得檔案名稱
    print('open file => ' + filename)                                          #顯示檔案路徑與名稱

def exit():                                                                    #自訂函式exit
    base.destroy()                                                             #destory方法會結束base視窗 

def find():                                                                    #自訂函式find
    print('find!')                                                             #顯示find!

menubar = tk.Menu(base)                                                        #主要作為選單項目放置的場所 
filemenu = tk.Menu(menubar)                                                    #以選單列為基礎製作檔案選單
menubar.add_cascade(label='File',menu=filemenu)                                #用add_cascade方法將filemenu與menubar建立關聯
filemenu.add_command(label='open',command=open)                                #用add_command方法新增選單列可點擊的項目,將label設定字串為open,command設定點擊後執行open函式
filemenu.add_separator()                                                       #filemenu內顯示格線
filemenu.add_command(label='exit',command=exit)                                #用add_command方法新增選單列可點擊的項目,將label設定字串為exit,command設定點擊後執行exit函式
editmenu = tk.Menu(menubar)                                                    #以選單列為基礎製作edit選單
menubar.add_cascade(label='Edit',menu=editmenu)                                #用add_cascade方法將editmenu與menubar建立關聯
editmenu.add_command(label='find',command=find)                                #用add_command方法新增選單列可點擊的項目,將label設定字串為find,command設定點擊後執行find函式 
base.config(menu=menubar)                                                      #將menubar配置在作為base的menu上
base.mainloop()                                                                #讓GUI介面可以顯示出來