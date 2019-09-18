class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x = {0}, y = {1}'.format(self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

def main():
    p1 = Point(12, 6)
    print(p1)
    p2 = Point(5, -12)
    print(p2)
    p3 = p1 + p2
    print(p3)

main()