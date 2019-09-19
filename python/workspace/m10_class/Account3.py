# 第二種寫法, 將balance設定傳參數, 預設參數為0

class Account:
    def __init__(self, number, name, balance = 0):
        self.number = number
        self.name = name
        self.balance = balance

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
    acc = Account('123456789', 'Tom', 10000)
    print(acc.number)
    print(acc.name)
    print(acc.balance)

    amount = int(input('輸入存款金額: '))
    acc.deposit(amount)
    print(acc.balance)
    amount = int(input('輸入提款金額: '))
    acc.withdraw(amount)
    print(acc.balance)

    print('-----------------------------------------------------------')

    acc1 = Account('987654321', 'Mary')
    print(acc1.number)
    print(acc1.name)
    print(acc1.balance)

    amount = int(input('輸入存款金額: '))
    acc1.deposit(amount)
    print(acc1.balance)
    amount = int(input('輸入提款金額: '))
    acc1.withdraw(amount)
    print(acc1.balance)

main()