# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:28:06 2019

@author: User
"""

#在畫面加上元件

import tkinter as tk                                                           #匯入tkinter模組別名tk
base = tk.Tk()                                                                 #透過tkinter將TK類別實體化
#def push():                                                                    #定義按鈕按下後要執行什麼
#    print("Let It GO~")
#button1 = tk.Button(base,text='白金不給加班費!',command=push).pack()              #command選項設定按鈕按下時的動作


#Label方法,text字串顯示,bg background設定背景顏色,width寬度,height高度,image設定圖片

tk.Label(base,text="紅",bg="red",width=20).pack()
tk.Label(base,text="綠",bg="green",width=20).pack()
tk.Label(base,text="藍",bg="blue",width=20).pack()
base.mainloop()