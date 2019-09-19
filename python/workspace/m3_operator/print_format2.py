a = 123
print(format(a, 'd')) # 10進位整數
print(format(a, '5d')) # 向右靠5位
print(format(a, '05d')) # 向右靠5位, 左邊補0
print(format(a, '2d')) # 向右靠2位
print(format(a, '<5d')) # 向左靠5位
print(format(a, 'x')) # 16進位小寫
print(format(a, 'X')) # 16進位大寫
print(format(a, '#x')) # 16進位小寫, 前面多0x
print(format(a, '#X')) # 16進位大寫, 前面多0x
print(format(a, 'o')) # 8進位小寫(沒大寫)
print(format(a, '#o')) # 8進位小寫(沒大寫), 前面多0x
print(format(a, 'd%%'))
print(format(a, '+d'))

a = -123
print(format(a, 'd'))

a = 12345.678
print(format(a, 'f'))
print(format(a, '.2f'))
print(format(a, '10.1f'))
print(format(a, '010.1f'))
print(format(a, '<10.1f'))
print(format(a, '10,.1f'))
print(format(a, 'e'))
print(format(a, 'E'))
print(format(a, '.2E'))
print(format(a, '10.2E'))


a = 'Python'
print(format(a, 's'))
print(format(a, '10s'))
print(format(a, '>10s'))
print(format(a, '^10s'))
print(format(a, '*^10s'))
print(format(a, '*>10s'))
print(format(a, '*<10s'))
"""
print('%r' % a) # 使用repr( )輸出
print('%10s %10s %10s' % (a, a, a))
print('%10s %10s %10s' % ('Python', 'Python', 'Python'))
print('%10s %10s %10s' % ('C++', 'C++', 'Java'))
print('%-10s %-10s %-10s' % ('Python', 'Python', 'Python'))
"""