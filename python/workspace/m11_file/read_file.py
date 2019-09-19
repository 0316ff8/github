with open('lang.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != "":
        print(line, end="")
        line = f.readline()
print('===================================')
with open('lang.txt', 'rt', encoding='utf-8') as f:
    line = f.readline()
    while line != "":
        print(repr(line[:-1]))
        line = f.readline()
print('===================================')
with open('lang.txt', encoding='utf-8') as f:
    data = f.read()
    print(data)
    print(repr(data[:-1]).replace('\\n', ','))
print('------------------------------------------------------------')
with open('lang.txt', encoding='utf-8') as f:
    print(f.read(12))
    print(f.read(10))
print('===================================')
with open('lang.txt', encoding='utf-8') as f:
    print(f.readlines())

with open('lang.txt', encoding='utf-8') as f:
    print(f.readlines(8))  # 按照字元數讀取，\n算一個字元，讀到最後一個字

print('===================================')
with open('lang.txt', encoding='utf-8') as f:
    print(f.read())
    f.seek(10)
    print(f.read())