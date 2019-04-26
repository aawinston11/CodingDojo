def type_list(list):
    sum = 0
    phrase = ""
    list_type = "The list you entered is of "
    for each in list:
        if isinstance(each, str):
            phrase += each + " "
        elif isinstance(each, int):
            sum += each
    if sum >0 and len(phrase)>0:
        list_type += "mixed type"
        list_type += "\nThe sum is " + str(sum)
        list_type += "\nThe string is " + phrase
    elif sum > 0:
        list_type += "integer"
        list_type += "\nThe sum is " + str(sum)
    elif len(phrase)>0:
        list_type += "string"
        list_type += "\nThe string is " + phrase
    print(list_type)
