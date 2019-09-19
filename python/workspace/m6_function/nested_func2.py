def outer():
    print('Jordan')
    def inner():
        print('Neymar')
        def inner1():
            print('Messi')
        inner1()
    inner()
outer()