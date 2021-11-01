def whileInputFunction ():
    while True:
        try:
            a = int(input("please enter A as a number: "))
            b = int(input("please enter B as a number: "))
            c = int(input("please enter C as a number: "))
            while a < b:
                print("a = ",a, "it`s < ",b,", need to plus: a + ",c)
                a += c
                if a == b:
                    a += c
                    print("a = b = ", b, ", need to plus: a + ", c)
            else:
                print(a, " > b")
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            break