# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:08:10 2019

@author: User
"""


"""
#CheckButton

import tkinter as tk                                                           #匯入tkinter模組別名tk
base = tk.Tk()                                                                 #透過tkinter將TK類別實體化
topping = {0:"海瓜子",1:"大甲蟹",2:"清蒸魚",3:"九孔"}                              #放入字典型態的資料
check_value={}                                                                 #建立空字典
for i in range(len(topping)):                                                  #用len計算元素的數量當作迴圈次數
    check_value[i] = tk.BooleanVar()                                           #將tk.BooleanVar類別設定給check_value變數,該類別值只有1(true)與0(false),故以此定義勾選傳回true
    tk.Checkbutton(base,variable=check_value[i],text=                          #variable值為1或0,用來判斷有沒有勾選,text為顯示字典topping的選單,anchor放置基礎視窗的左側(West西)
                   topping[i]).pack(anchor=tk.W)
    
def buy():                                                                     #自訂buy函式
    for i in check_value:                                                      #for迴圈將字典(菜單)中的布林值(value)傳到i中
        if check_value[i].get() == True:                                       #如果用get方法取出的值等於True
            print(topping[i])                                                  #顯示字典內的品名(value)
            
tk.Button(base,text="點菜",command=buy).pack()                                  #自訂按鈕顯示點菜,command選項執行buy函式
base.mainloop()                                                                #讓GUI介面可以顯示出來
"""

#RadioButton(只能單選)

import tkinter as tk                                                           #匯入tkinter模組別名tk
base = tk.Tk()                                                                 #透過tkinter將TK類別實體化
radio_value = tk.IntVar()                                                      #通過tk.IntVar()獲取單選按鈕value值更新
radio_value.set(0)                                                             #預設選擇字典0的選項A套餐
lunch = {0:"A套餐",1:"B套餐",2:"C套餐"}                                          #放入字典型態的資料 
tk.Radiobutton(base,text=lunch[0],variable=radio_value,value=0).pack()         #新增按鈕,text顯示A套餐字串,variable儲存按鈕選取的操作狀態,value設定該項目的值
tk.Radiobutton(base,text=lunch[1],variable=radio_value,value=1).pack()
tk.Radiobutton(base,text=lunch[2],variable=radio_value,value=2).pack()

def buy():                                                                     #自訂buy函式
    value = radio_value.get()                                                  #使用get方法將radio_value的值傳到value中
    print(lunch[value])                                                        #顯示字典內的品名(value) 
    
tk.Button(base,text="點菜",command=buy).pack()                                  #自訂按鈕顯示點菜,command選項執行buy函式 
base.mainloop()                                                                #讓GUI介面可以顯示出來