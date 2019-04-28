def make_dict(list1, list2):
    new_dict={}

    if len(list1)>=len(list2):
        for x in range(0, len(list1)):
            new_dict[list1[x]] = list2[x]
    elif len(list1)<len(list2):
        for x in range(0, len(list1)):
            new_dict[list2[x]] = list1[x]

    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print make_dict(name, favorite_animal)