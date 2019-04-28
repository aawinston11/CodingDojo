def star(list):
    for i in list:
        print "*" * i

star([1,2,3,4,5])

def stars(list):
    for i in range(len(list)):
        star_line= ""
        if isinstance(list[i], int):
            for i in range(list[i]):
                star_line += "*"
            print star_line
        elif isinstance(list[i], str):
            letter = list[i][0].lower()
            for x in range(len(list[i])):
                star_line+=letter
            print star_line

stars([1,2,3, "Peter", "Will", 6, "FEEEEETTTT",3,4,5])
