class Call(object):
    def __init__(self, callid, name, number, time, reason):
        self.id = callid
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print "ID: {}\nName: {}\nPhone Number: {}\nTime: {}\nReason: {}\n".format(self.id, self.name, self.number, self.time, self.reason)

class callCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)

    def add(self, newCall):
        self.calls.append(newCall)
        self.queue += 1
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue -= 1
        return self

    def info(self):
        text = ""
        for each in self.calls:
            text += each.name + " " + str(each.number) + "\n"
        text += "Queue: " + str(self.queue) + "\n"
        print text
        return self

    def find_remove(self, phone_num):
        for each in range(0, len(self.calls)):
            for attr in self.calls:
                if attr.number == phone_num:
                    self.calls.pop(each)
        return self
    
    
  
    

call = Call("1", "Sam", "4105859696", "12:30PM", "Emergency")
callb = Call("2", "Tony", "9809856265", "4:30AM", "Inquiry")

# call.display()
# callb.display()

callCenter1 = callCenter()
callCenter1.add(call)
callCenter1.add(callb)
callCenter1.info()
callCenter1.remove()
callCenter1.info()
callCenter1.add(call)
callCenter1.info()
