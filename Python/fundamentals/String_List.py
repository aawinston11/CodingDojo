def find_replace():
    words = "It's thanksgiving day. It's my birthday,too!"
    print words.find('day')
    month = words
    print month.replace('day', 'month')
 find_replace()

def max_min():
    x=[2,54,-2,7,12,98]
    print min(x)
    print max(x)
# max_min()

def first_last():
    x = ["hello",2,54,-2,7,12,98,"world"]
    print x[0]
    print x[len(x)-1]
# first_last()

def new_list():
    x = [19,2,54,-2,7,12,98,32,10,-3,6]
    x.sort()
    split_back = x[len(x)/2:]
    split_back.insert(0, x[:len(x)/2])
    print split_back
new_list()