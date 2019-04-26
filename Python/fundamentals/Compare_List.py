def compareList(list_a, list_b):
    compare = 0
    if (len(list_a) == len(list_b)):
        for x in range (0, len(list_a)):
            if list_a[x]==list_b[x]:
                compare += 1
        if compare==len(list_a):
            print "The lists are the same"
        else:
            print "The lists are not the same"
    else:
        print "The lists are not the same"       

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_1 = [1,2,5,6,5]
list_2 = [1,2,5,6,5]

list_o = [1,2,5,6,5,16]
list_t = [1,2,5,6,5]

list_a = ['celery','carrots','bread','milk']
list_b = ['celery','carrots','bread','cream']

compareList(list_one, list_two)
compareList(list_1, list_2)
compareList(list_a, list_b)
compareList(list_o, list_t)