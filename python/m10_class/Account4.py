# 使用__str__( ),讓print( )列印物件為想要的結果
# P153-P154

class Account:
    def __init__(self, number, name, balance):
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
    def __str__(self):
        return 'number : {0}, name: {1}, balance:{2}'.format(self.number,self.name,self.balance)

