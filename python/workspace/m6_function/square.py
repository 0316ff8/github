def square(x):
    return x * x

def total(a, b):
    return a + b

def main():
    result = square(3)
    print(result)
    print(square(5))
    a, b = eval(input('input two  number:'))
    print(total(a, b))
main()


