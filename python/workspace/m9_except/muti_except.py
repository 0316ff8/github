# 多種異常處理
# P143-P144
try:
    n1, n2 = eval(input("Enter two numbers to divide:"))
    div = n1 / n2
    print('%d / %d = %d' %(n1, n2, div))
except ZeroDivisionError:
    print('ZeroDivisionError')  # 不能除以0
except SyntaxError:
    print('SyntaxError')       # 文法錯誤, 例如:沒逗號
except:
    print('Something Wrong')  # 未知錯誤
else:
    print('No exception')      # 沒錯誤
finally:
    print('Must be done')
