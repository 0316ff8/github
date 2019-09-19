# 使用raise丟出異常
# P142
try:
    num = int(input("輸入一介於0-100的分數:"))
    if num < 0 or num >100:
        raise ValueError
    else:
        print('分數為:', num)
except ValueError:
    print('請輸入介於0-100的分數')