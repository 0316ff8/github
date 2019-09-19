# 預設引數值(參數)
# P88
def sum_avg(n1, n2=100):
    total = 0
    for i in range(n1, n2+1):
        total += i
    avg = total/(n2-n1+1)
    return total, avg

def main():
    total, avg = sum_avg(1) # n1=1, n2沒給值用預設值100
    print('sum = {0}, average = {1}'.format(total, avg))
    total, avg = sum_avg(1, 50)
    print('sum = {0}, average = {1}'.format(total, avg))

main()