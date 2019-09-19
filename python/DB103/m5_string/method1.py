# 判斷是否為字母或數字所組成
s1 = 'abc'
s2 = '123'
s3 = 'abc123'
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())

print('-----------------------------')

# 判斷識別字 - 對照講義P34
print(s1.isidentifier())
print(s2.isidentifier())
print(s3.isidentifier())
print('a-1'.isidentifier())
print('_1'.isidentifier())
print('@'.isidentifier())

print('-----------------------------')

# 判斷大小寫
s1 = 'abc'
s2 = 'ABC'
s3 = 'aBC'
print(s1.islower())
print(s2.islower())
print(s3.islower())
print(s1.isupper())
print(s2.isupper())
print(s3.isupper())

print('-----------------------------')

# 判斷是否為空白字元
print(''.isspace())
print(' '.isspace())
print('\n'.isspace())
print('\t'.isspace())