# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:29:19 2019

@author: User
"""

import qrcode as qr                                                            #匯入qrcode模組  
import tkinter as tk                                                           #匯入tkinter模組別名tk
import tkinter.filedialog as fd                                                #匯入tkinter.filedialog模組別名fd
from PIL import ImageTk                                                        #從外部函式庫Pillow載入ImageTk模組,將圖片轉為可在tkinter中使用的格式

base = tk.Tk()
base.title('QRcode Generator')                                                 #視窗最上方顯示 QRcode Generator    
input_area = tk.Frame(base,relief=tk.RAISED,bd=2)                              #放置要轉為QRCode的字串及按鈕,relief為按鈕樣式,RAISED為凸起,bd為borderwidth邊框寬度
image_area = tk.Frame(base,relief=tk.SUNKEN,bd=2)                              #定義放置QRCode圖片區域,,relief為按鈕樣式,SUNKEN為凹陷,bd為borderwidth邊框寬度
encode_text = tk.StringVar()                                                   #儲存要轉換成QR Code的字串
entry = tk.Entry(input_area,textvariable=encode_text).pack(side=tk.LEFT)       #實體化Entry類別建立輸入框,輸入框配置位置為input_area設定,顯示內容在上行的encode_text,靠左排列
qr_label = tk.Label(image_area)                                                #顯示QRCode的標籤

def generate():                                                                #自訂函式generate
    qr_label.qr_img = qr.make(encode_text.get())                               #透過get函式取得要轉成QRCode的字串,利用qrcode套件的make函式生成圖片,傳給qr_label的qr_img
    img_width,img_height = qr_label.qr_img.size                                #qr_img.size回傳儲存高度寬度資訊的Tuple型態資料,程式分別存入左側兩個變數中
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)                      #透過Pillow的ImageTk模組將qrcode套件產生的圖片轉換成tkinter可顯示的資料
    qr_label.config(image=qr_label.tk_img,width=img_width,height=img_height)   #定義qr_label設定各種選項,可透過config函式為設定項目設定值
    qr_label.pack()
    
encode_button = tk.Button(input_area,text='QRcode!',command=generate).pack(side=tk.LEFT)#建立QRCode按鈕,按下去執行generate函式,靠左側排列
input_area.pack(pady=5)                                                        #padx,pady設定與邊框間距
image_area.pack(padx=3,pady=1)                                                 #padx,pady設定與邊框間距                                       

def save():                                                                    #自訂函式save
    filename = fd.asksaveasfilename(title='命令後進行儲存',initialfile='qrcode.png')#使用asksaveasfilename函式,title設定儲存視窗標題為'命令後進行儲存',initialfile設定存檔的檔名
    if filename and hasattr(qr_label,'qr_img'):                                #判斷式判斷有filename為True,hasattr函式驗證第一個參數存在第二個參數的attribute,存在為True,
        qr_label.qr_img.save(filename)                                         #兩者皆為True才會取得檔案名稱儲存QRCode圖片

def exit():                                                                    #自訂函式exit  
    base.destroy()                                                             #destory方法會結束base視窗 
    
menubar = tk.Menu(base)                                                        #主要作為選單項目放置的場所 
filemenu = tk.Menu(menubar)                                                    #以選單列為基礎製作檔案選單
menubar.add_cascade(label='File',menu=filemenu)                                #用add_cascade方法將filemenu與menubar建立關聯
filemenu.add_command(label='save',command=save)                                #用add_command方法新增選單列可點擊的項目,將label設定字串為open,command設定點擊後執行open函式
filemenu.add_separator()                                                       #filemenu內顯示格線
filemenu.add_command(label='exit',command=exit)                                #用add_command方法新增選單列可點擊的項目,將label設定字串為exit,command設定點擊後執行exit函式
base.config(menu=menubar)                                                      #將menubar配置在作為base的menu上
base.mainloop()                                                                #讓GUI介面可以顯示出來

