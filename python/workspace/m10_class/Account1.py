# 第一種寫法
# P149-P150
class Account:
    pass
def deposit(acc, amount):
    try:
        if amount <= 0:
            raise ValueError
        acc.balance += amount
    except ValueError:
        print('金額必須為正整數')
def withdraw(acc, amount):
    try:
        if amount <= acc.balance:
            acc.balance -= amount
        else:
            raise ValueError
    except ValueError:
        print('餘額不足')

def main():
    acc = Account()
    acc.number = '123456789'
    acc.name = 'Tom'
    acc.balance = 0

    print(acc.number)
    print(acc.name)

    amount = int(input('輸入存款金額: '))
    deposit(acc, amount)
    print(acc.balance)
    amount = int(input('輸入提款金額: '))
    withdraw(acc, amount)
    print(acc.balance)

main()