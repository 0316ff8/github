# 異常處理
# P138-P141
'''
num = int(input("輸入整數:"))
print('{}為{}'.format(num, '奇數' if num % 2 else '偶數'))

try:
    num = int(input("輸入整數:"))
    print('{}為{}'.format(num, '奇數' if num % 2 else '偶數'))
except ValueError as e:
    print(e)    # 印ValueError的錯誤訊息
'''

try:
    num = int(input("輸入整數:"))
    print('{}為{}'.format(num, '奇數' if num % 2 else '偶數'))
except ValueError:
    print('請輸入阿拉伯數字')