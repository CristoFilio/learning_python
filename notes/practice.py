choices = "1. Read python,2. Learn python,3. Watch python,4. see Python,5. Misspell Python".split(",")
selection = 9999
while int(selection) != 0:
    if selection not in [choice[0] for choice in choices] and int(selection) != 0:
        print("Select and option typing the number\n")
        for x in choices:
            print(x)
        selection = input()
    else:
        for x in choices:
            print(x)
            if selection == x[0]:
                print("You selected {}\n".format(x))
                selection = 99999
                break
else:
    print('Terminated')



