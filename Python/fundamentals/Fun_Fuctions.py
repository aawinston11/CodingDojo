def oddEven(num):
    for i in range(1, num+1):
        if i%2==0:
            print "Number is " + str(i) + ". " + "This is an even number."
           
        elif i%2!=0:
            print "Number is " + str(i) + ". " + "This is an odd number."
oddEven(200)

def multiply(list,num):
    newArr=[]
    for each in range(0, len(list)):
        arr = list[each] * num
        newArr.append(arr)
    return newArr
print multiply([1,2,3,4,5],3)

def hacker(arr):
    listNew=[]
    for each in arr:
        arr_a=[]
        for i in range(0,each):
            arr_a.append(1)
        listNew.append(arr_a)
    return listNew
print hacker(multiply([1,2,3,4,5], 3))