from m10_class.Account4 import Account
from m10_class.CheckingAccount import CheckingAccount

def main():

    # acc = Account('123456789', 'Tom')
    # acc.deposit(5000)
    # print(acc)
    # acc.withdraw(2000)
    # acc.name = 'Mary'
    # print(acc)
    #
    # acc = Account("6654778", "Stephen", 10000)
    # acc.deposit(6000)
    # acc.withdraw(5000)
    # print(acc)

    ca = CheckingAccount("44455566", "Stephen", 10000)
    ca.deposit(5000)
    ca.withdraw(2000)
    print(ca)

    ca1 = CheckingAccount("44455456", "Maria", 10000)
    ca1.deposit(5000)
    ca1.withdraw(23000)
    print(ca1)

main()