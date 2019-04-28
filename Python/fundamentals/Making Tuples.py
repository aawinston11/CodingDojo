def making_tupes(dict):
    myList = []
    
    for key, value in dict.iteritems():
        myList.append((key,value))
    return myList

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print making_tupes(my_dict)