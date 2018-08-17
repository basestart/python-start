class Animal(object):
    def run(self):
        print 'animal running'

class Dog(Animal):
    def run(self):
        print 'Dog is running'

class Cat(Animal):
    def run(self):
        print 'Cat is running'


def runTwice(animal):
    animal.run()
    animal.run()

runTwice(Animal())
runTwice(Dog())
runTwice(Cat())

print dir(Animal())
# dog = Dog()
# cat = Cat()

# dog.run()
# cat.run()