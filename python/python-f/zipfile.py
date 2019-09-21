#Python zip Unzip


#import zipfile
#files = zipfile.ZipFile('C:\python\sfs.zip')    #讀取zipfile壓縮檔，要完整路徑含檔名
#files.namelist()                                #查看壓縮檔裡面的檔案名稱
#files.extract('sfs.rtf',r'C:\python')           #解壓縮檔案('檔案名稱',r'檔案路徑')
#files.extractall('C:\python')                   #解壓縮所有檔案('檔案路徑')
#files.close()                                   #關閉模組




import zipfile
zip_files = zipfile.ZipFile('C:\\python\\123.zip',mode='w')    #指定壓縮後的檔案名稱，要完整路徑含檔名，反斜線要兩個，對zipfile開啟寫入模式
zip_files.write('C:\\python\\456.txt','333.txt')               #寫入檔案456.txt寫入zipfile，檔名改成333.txt
zip_files.close()                                              #關閉模組
file = zipfile.ZipFile('C:\\python\\123.zip')                  #讀取zipfile壓縮檔，要完整路徑含檔名
file.namelist()                                                #查看壓縮檔裡面的檔案名稱