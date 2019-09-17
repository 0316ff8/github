# 回傳多個值的函式
# P87
def sum_avg(n1, n2):
    total = 0
    for i in range(n1, n2+1):
        total += i
    avg = total/(n2-n1+1)
    return total, avg

def main():
    total, avg = sum_avg(1, 100)
    print('sum = {0}, average = {1}'.format(total, avg))

main()