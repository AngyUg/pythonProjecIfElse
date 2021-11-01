def ifElseInput(a=int, b=int):
    while True:
        try:
            a = int(input("please enter A as a number: "))
            b = int(input("please enter B as a number: "))
            if a < b:
                print("It`s terrible :-( a: ", a, " < ", "b: ", b)
            elif a > b:
                print("a: ", a, " > ", "b: ", b)
            else:
                print("Exciting, :-)  a: ", a, " = ", "b: ", b)
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            break
