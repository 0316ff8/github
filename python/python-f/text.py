# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:16:38 2019

@author: User
"""

#Text輸入框

import tkinter as tk                                                           #匯入tkinter模組別名tk
base = tk.Tk()                                                                 #透過tkinter將TK類別實體化
string = tk.StringVar()
entry = tk.Entry(base,textvariable=string).pack()
label = tk.Label(base,textvariable=string).pack()

base.mainloop()                                                                #讓GUI介面可以顯示出來