string = map(str,raw_input().split())
change = 0

if len(string[0]) != 1:
    # if only contains uppercase leters
    for letter in string[0]:
        if letter == letter.upper():
            change = 1
        else:
            change = 0
            break

    # if all letters except for the first one are uppercase
    if change == 0:
        if string[0][0].islower():
            for letter in string[0][1:]:
                if letter.isupper():
                    change = 2
                else:
                    change = 0
                    break

    def changestring(string,change):
        if change != 0:
            if change == 2:
                string[0] = string[0].lower()
                print string[0][0].upper() + string[0][1:]
            elif change == 1:
                print string[0].lower()
        else:
            print string[0]

    changestring(string,change)
else:
    if string[0].islower():
        print string[0].upper()
    else:
        print string[0].lower()
