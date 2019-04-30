class Car(object):
    def __init__(self, price, speed, fuel,  mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if mileage > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

        self.displayAll()
    def displayAll(self):
        print "Price: " , self.price
        print "Speed: " , self.speed, "mph"
        print "Fuel: " , self.fuel, "miles per gallon"
        print "Mileage: " , self.mileage, "mpg"
        print "Tax: " , self.tax * 100, "%"

Ford = Car(45000,130,22,2500)
Chevy    = Car(8500,140,6,150000)
Honda      = Car(20000,130,8,75000)
Toyota      = Car(12000,140,20,275000)
Acura     = Car(30000,280,18,25000)
Audi      = Car(80000,200,4,30000)