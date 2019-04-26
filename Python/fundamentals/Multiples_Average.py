def odd_numbers():
    for odd in range(1, 1000):
        if odd%2 != 0:  
            print odd
# odd_numbers()

def multiples_five():
    for x in range(5, 1000000):
        if x%5 == 0:
            print x
# multiples_five()

def sum_list():
    a = [1, 2, 5, 10, 255, 3]
    print sum(a)
sum_list()

def average_list():
    a = [1, 2, 5, 10, 255, 3]
    print sum(a)/len(a)
average_list()