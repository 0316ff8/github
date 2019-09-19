a = 123
print('%d' % a) # 10進位整數
print('%5d' % a) # 向右靠5位
print('%05d' % a) # 向右靠5位, 左邊補0
print('%2d' % a) # 向右靠2位
print('/' + '%-5d' % a + '/') # 向左靠5位

print('%x' % a) # 16進位小寫
print('%X' % a) # 16進位大寫
print('%#x' % a) # 16進位小寫, 前面多0x
print('%#X' % a) # 16進位大寫, 前面多0x
print('%o' % a) # 8進位小寫(沒大寫)
print('%#o' % a) # 8進位小寫(沒大寫), 前面多0x
print('%d%%' % a)
print('%+d' % a)

a = -123
print('%d' % a)

a = 12345.678
print('%f' % a)
print('%.2f' % a) #
print('%.1f' % a) #
print('%10.1f' % a) #
print('%010.1f' % a)
print('%-10.1f' % a)
print('%e' % a)
print('%E' % a)
print('%.2E' % a)
print('%10.2E' % a)

a = 'Python'
print('%s' % a)
print('%10s' % a)
print('%-10s' % a)
print('%r' % a) # 使用repr( )輸出
print('%10s %10s %10s' % (a, a, a))
print('%10s %10s %10s' % ('Python', 'Python', 'Python'))
print('%10s %10s %10s' % ('C++', 'C++', 'Java'))
print('%-10s %-10s %-10s' % ('Python', 'Python', 'Python'))