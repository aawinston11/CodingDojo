class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def displayInfo(self):
        print "Price:{} \nName: {} \nWeight: {}\nBrand: {} \nCost: {} \nStatus: {} \n".format(self.price, self.name, self.weight, self.brand, self.cost, self.status)
        return self

    def sell(self):
        self.status = "Sold"
        return self
    
    def addTax(self, tax):
        tax = tax / 100
        salesTax = self.price * tax
        self.price = salesTax + self.price
        return self
    
    def itemReturn(self, reason_return):
        if reason_return == "defective":
            self.status = reason_return
            self.price = 0
        elif reason_return == "in box":
            self.status = "For Sale"
        elif reason_return == "opened":
            self.status = "Used"
            self.cost *= .8
        return self

soda = Product(6, "Soda", 1, "Fanta", 6)
soda.displayInfo()
soda.sell()
soda.itemReturn("opened").displayInfo()