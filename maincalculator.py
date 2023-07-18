def restart():


    # which calculation you like to perform?
    def calc():
        print('Which mathematical operation would you like to use?')
        operations = ('1: Addition', '2: Subtraction', '3: Multiplication', '4: Division')
        for item in operations:
            print(item)
        global operationchoice
        operationchoice = input('enter choice 1/2/3/4: ')
        if operationchoice == "1":
            print('choose 2 numbers to add')
        elif operationchoice == "2":
            print('choose 2 numbers to subtract')
        elif operationchoice == "3":
            print("choose 2 numbers to multiply")
        elif operationchoice == "4":
            print("choose 2 numbers to divide:")
        else:
            print("number not found please try again")
            import time
            time.sleep(1.5)
            calc()
    calc()


    # selecing the digits
    def digits():
        global firstdigit
        global seconddigit
        firstdigit = input('enter first number: ')
        seconddigit = input('enter second number: ')
    digits()


    # digit checker
    if not firstdigit.isnumeric() or not seconddigit.isnumeric():
        if True:
            import time
            time.sleep(1)
            print('invalid set of numbers')
            time.sleep(1)
            print('please try again')
            time.sleep(1)
            digits()


    # operation
    if operationchoice == "1":
        sum = (float(firstdigit)) + (float(seconddigit))
        print("Sum = " + (str(sum)))
    elif operationchoice == "2":
        difference = (float(firstdigit)) - (float(seconddigit))
        print("Difference = " + (str(difference)))
    elif operationchoice == "3":
        product = (float(firstdigit)) * (float(seconddigit))
        print("Product = " + (str(product)))
    elif operationchoice == "4":
        quotient = (float(firstdigit)) / (float(seconddigit))
        print("Quotient = " + (str(quotient)))


    # finished? or not?
    def finished():
        import time
        time.sleep(1.5)
        done = input("would you like to try a new equation? Y/N: ")
        if done.lower() == "y":
            restart()
        elif done.lower() == "n":
            print('GOODBYE')
            exit()
        else:
            print ("try again")
            time.sleep(1)
            finished()
    finished()

restart()