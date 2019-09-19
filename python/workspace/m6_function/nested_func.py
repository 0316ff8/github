# P92 巢狀函式
def outer(msg):
    def inner():
        print(msg)
    inner()
outer('Hello')