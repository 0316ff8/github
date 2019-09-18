# 關鍵字引數(參數)
# P89
def msg(name, age):
    print('{0} is {1} years old!'.format(name, age))
msg('Tom', 30)
msg(name='Tom',age=30)
msg(age=30, name='Tom')
msg('Tom', age=30)
# msg(name='Tom', 30) 引數不能放前面