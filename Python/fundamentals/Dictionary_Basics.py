new_dict = {
    "name": "Andre", 
    "age": 30, 
    "state of birth": "Oklahoma", 
    "favorite color": "blue"
}

def printDict(newDict):
    for key, value in newDict.iteritems():
            print "My " + key + " is " +str(value)
printDict(new_dict)