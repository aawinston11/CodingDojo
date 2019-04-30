class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayInfo(self):
        print "Name: {} \nHealth: {}".format(self.name, self.health)
        return self
    
animal = Animal("Pete", 200)
animal.walk().walk().walk().run().run().displayInfo()

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet (self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayInfo(self):
        super(Dragon, self).displayInfo()
        print "I am a dragon"

dog = Dog("Koda", 0)
dog.walk().walk().walk().run().run().pet().displayInfo()

dragon = Dragon("Flame", 0)
dragon.run().run().fly().fly().fly().displayInfo()
