def calc():
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))
    choice = input("1.Addition , 2.Subtraction , 3.Multiplication , 4.Division")
    if choice == "1":
        Addition = num1 + num2
        print (f"added value is:{Addition}")
    elif choice =="2":
        Subtraction = num1 - num2
        print (f"subtracted value is:{Subtraction}")
    elif choice == "3":
        Multiplication = num1 * num2
        print(f"product value is:{Multiplication}")
    elif choice == "4":
        if num2 == 0:
            print("can't divide by zero")
        else:
            Division = num1 / num2
            print(f"divided value is: {Division}")
calc()
    
