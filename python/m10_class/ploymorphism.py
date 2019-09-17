class Dog:
    def run(self):
        print("Dog: run( )")
    def walk(self):
        print("Dog: walk( )")

class Cat:
    def run(self):
        print("Cat: run( )")
    def walk(self):
        print("Cat: walk( )")

class Horse:
    def run(self):
        print("Horse: run( )")
    def walk(self):
        print("Horse: walk( )")


def main():
    dog = Dog()
    dog.run()
    dog.walk()

    cat = Cat()
    cat.run()
    cat.walk()

    horse = Horse()
    horse.run()
    horse.walk()


# interface
def test(animal):
    animal.run()
    animal.walk()

def main():
    dog = Dog()
    test(dog)
    cat = Cat()
    test(cat)
    horse = Horse()
    test(horse)


main()