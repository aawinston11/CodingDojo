def filter_type(info):
    #filter for integer
    if isinstance(info, int):
        if info >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"

    #filter for string
    elif isinstance(info, str):
        if len(info) >=50:
            print "Long sentence."
        else:
            print "Short sentence."

    #filter for list
    elif isinstance(info, list):
        if len(info) >= 10:
            print "Big list!"
        else:
            print "Short list."

#dojotest
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

filter_type(sI)
filter_type(mI)
filter_type(bI)
filter_type(eI)
filter_type(spI)
filter_type(sS)
filter_type(mS)
filter_type(bS)
filter_type(eS)
filter_type(aL)
filter_type(mL)
filter_type(lL)
filter_type(eL)
filter_type(spL)