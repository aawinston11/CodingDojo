class mathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, num, *numa):
        if (isinstance (num, list)) or (isinstance (num, tuple)):
            for each in num:
                self.result += each
        else:
            self.result += num

        for each in numa:
            if (isinstance (each, list)) or (isinstance(each, tuple)):
                for every in each:
                    self.result += every 
            else:
                self.result += each
        
        return self

    def sub(self, num, *numa):
        if (isinstance (num, list)) or (isinstance (num, tuple)):
            for each in num:
                self.result -= each
        else:
            self.result -= num

        for each in numa:
            if (isinstance (each, list)) or (isinstance(each, tuple)):
                for every in each:
                    self.result -= every 
            else:
                self.result -= each
        
        return self

md = mathDojo().add(2).add(2,5).sub(3,2).result
mda = mathDojo().add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).sub(2, [2,3], [1.1,2.3]).result

print md
print mda
