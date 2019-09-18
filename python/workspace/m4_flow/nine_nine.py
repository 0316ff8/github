# 九九乘法表

for i in range(1, 10):
    for j in range(1, 10):
        print('{0}*{1}={2}'.format(i, j, i*j), end='\t')
    print()
print("------------------------------------------------------------------------------")
for i in range(1, 10):
    for j in range(1, 10):
        print('{0}*{1}={2}'.format(j, i, i*j), end='\t')
    print()