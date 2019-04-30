class Bike(object):
    def __init__(self, price, maxSpeed):
        self.price = price
        self.maxSpeed = maxSpeed
        self.miles = 0
    
    def display(self):
        print self.price, self.maxSpeed, self.miles
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(250, 10)
bike1.ride().ride().ride().reverse().display()

bike2 = Bike(300, 25)
bike2.ride().ride().reverse().reverse().display()

bike3 = Bike(400, 50)
bike3.reverse().reverse().reverse().display()