class A():
    def m1(self):
        print("A:m1( )")
    def m2(self):
        print("A:m2( )")

class B(A):
    def m3(self):
        print("B:m3( )")

class C(A):
    def m2(self):
        print("C:m2( )")
    def m3(self):
        print("C:m3( )")

class D(B, C):
    def m4(self):
        print("D:m4( )")

def main():
    d = D()
    d.m4()
    d.m3()
    d.m2()
    d.m1()

main()