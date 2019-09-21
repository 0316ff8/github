# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:03:28 2019

@author: User
"""

import tkinter as tk                                                           #匯入tkinter模組別名tk
base = tk.Tk()                                                                 #透過tkinter將TK類別實體化
#button1 = tk.Button(base,text='白金不給加班費!')                                 #新增按鈕定義按鈕項目,如：名稱 
#button2 = tk.Button(base,text='高雄發大財!')
#button3 = tk.Button(base,text='我是鋼鐵人!')
#button1.pack()                                                                 #顯示按鈕
#button2.pack()
#button3.pack()
#base.mainloop()                                                                #讓GUI介面可以顯示出來


#button1 = tk.Button(base,text='白金不給加班費',width=20).pack()                   #新增按鈕,定義按鈕項目,如：名稱,寬度..
#button2 = tk.Button(base,text='高雄發大財').pack(side=tk.LEFT)                   #後面新增.pack()可省略之後button.pack()
#button3 = tk.Button(base,text='我是鋼鐵人').pack(side=tk.RIGHT)                  #.pack()內可透過side排列方向


#grid方法,用列(row)與行(column)來設定元件位置

#button1 = tk.Button(base,text='白金不給加班費')
#button2 = tk.Button(base,text='高雄發大財')
#button3 = tk.Button(base,text='我是鋼鐵人')
#button1.grid(row=0,column=0)
#button2.grid(row=1,column=1)
#button3.grid(row=1,column=0)


#place方法,用座標來設定元件位置

button1 = tk.Button(base,text='白金不給加班費')
button2 = tk.Button(base,text='高雄發大財')
button3 = tk.Button(base,text='我是鋼鐵人')
button1.place(x=0,y=0)
button2.place(x=50,y=30)
button3.place(x=100,y=60)


base.mainloop() 