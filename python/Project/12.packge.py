# 主程式
# import 封包名稱.模組名稱
import geometry.point
result=geometry.point.distance(3,4)
print("距離",result)
import geometry.line
result=geometry.line.slope(1,1,3,3)
print("斜率",result)
# import 封包名稱.模組名稱 as 模組別名
# 用【別名】代替【封包名稱.模組名稱】
import geometry.line as line
result=line.len(1,1,4,4)
print("長度",result)