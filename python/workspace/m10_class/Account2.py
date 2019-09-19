# 第二種寫法
# P151-P152
class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0

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
    acc = Account('123456789', 'Tom')
    print(acc.number)
    print(acc.name)

    amount = int(input('輸入存款金額: '))
    acc.deposit(amount)
    print(acc.balance)
    amount = int(input('輸入提款金額: '))
    acc.withdraw(amount)
    print(acc.balance)

main()