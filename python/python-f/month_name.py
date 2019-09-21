# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:02:53 2019

@author: User
"""

def taiwan(month):
    month_name = {
            1:"一月",2:"二月",3:"三月",4:"四月",5:"五月",6:"六月",7:"七月",8:"八月",
            9:"九月",10:"十月",11:"十一月",12:"十二月"}
    try:
        #有可能會發生例外狀況的程式段落
        response = month_name[month]
    except:
        #發生例外時要如何處理
        response = "請輸入月份數字。"
    #整個函式最後以return回傳response,將資料回復至呼叫此函數的地方    
    return response
#使用者直接執行month_name.py這個檔案時會跳出 此為模組檔案，請import模組後再使用
if __name__ == "__main__":
    print("此為模組檔案，請import模組後再使用")