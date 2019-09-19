def greet(*names):
    for name in names:
        print('Hello,', name)
greet('Messi', 'Neymar', 'Jordan', 'Othani')


def stu(**data):
    for key, value in data.items():
        print("{} is {}".format(key, value))
stu(name="Tom", age="25", mobile="0934111222")
stu(name="Messi",email="messi@gmail.com", age="25", mobile="0934111222")