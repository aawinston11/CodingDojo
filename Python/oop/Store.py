class store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def remove_product(self, remove_product):
        remove_index = self.products.index(remove_product)
        self.products.pop(remove_index)
        return self

    def inventory(self):
        info = ""
        for each in self.products:
            info += "Product Name: " + each + "\n"
            info += "Location: " + self.location + "\n"
            info += "Owner: " + self.owner + "\n"
        print info
        return self

