# 使用__str__( ),讓print( )列印物件為想要的結果,(傳三個參數)
# P151-P152
class Account:
    def __init__(self, number, name, balance=0):
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

def main():
    acc = Account('123456789', 'Tom' )
    acc.deposit(5000)
    print(acc)
    acc.withdraw(2000)
    acc.name = 'Mary'
    print(acc)
    acc = Account('123987', 'Curry', 10000)
    print(acc)
main()