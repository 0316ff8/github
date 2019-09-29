getwd() # 看預設路徑
setwd("E:/R/riii/data") # 設定預設路徑
test.data = read.csv("./2330.csv", header = TRUE) # 將檔案讀取後放入test.data中
test.data # 看test.data資料
class(test.data)
str(test.data) # 看test.data結構
tdate = as.Date(test.data$Date)
class(tdate)
as.Date(tdate)[1] # 看test.data第一筆資料日期
as.Date(tdate) > "2018-01-01" # 看test.data哪個日期大於"2018-01-01"是對的

#date2017 = test.data[tdate >= "2017-01-01" & tdate <= "2017-12-31",]
#date2017
test.data[tdate >= "2017-01-01" & tdate <= "2017-12-31",]
max(date2017$Close)

test.data[which((test.data[tdate >= "2017-01-01" & tdate <= "2017-12-31",])$'Close' == max(date2017$Close))]

# a = test.data[(test.data[tdate >= "2017-01-01" & tdate <= "2017-12-31"]), max(date2017$Close)]

