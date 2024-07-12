def basemath():
    user_number = int(input("enter the first number:"))
    print(" reference for choice: +, -, *, /")
    user_operator = str(input("enter your math operation:"))
    user_number2 = int(input("enter second number:"))

    if user_operator == "+":
        user_result = user_number + user_number2
        print("result:", user_result)
        print("______________________________________")
        print("Do a new operation?: write 'y' if yes or something if no")
        user_reset = str(input(""))
        if user_reset == "y":
            print("______________________________________")
            basemath()
        else:
            pass

    elif user_operator == "-":

        user_result = user_number - user_number2
        print("result:", user_result)
        print("______________________________________")
        print("Do a new operation?: write 'y' if yes or something if no")
        user_reset = str(input(""))
        if user_reset == "y":
            print("______________________________________")
            basemath()
        else:
            pass

    elif user_operator == "*":
        user_result = user_number * user_number2
        print("result:", user_result)
        print("______________________________________")
        print("Do a new operation?: write 'y' if yes or something if no")
        user_reset = str(input(""))
        if user_reset == "y":
            print("______________________________________")
            basemath()
        else:
            pass

    elif user_operator == "/":
        user_result = user_number / user_number2
        print("result:", user_result)
        print("______________________________________")
        print("Do a new operation?: write 'y' if yes or something if no")
        user_reset = str(input(""))
        if user_reset == "y":
            print("______________________________________")
            basemath()
        else:
            pass
    else:
        print("______________________________________")
        print("Operation Error! Try again.")
        print("______________________________________")
        print("Do a new operation?: write 'y' if yes or something if no")
        user_reset = str(input(""))
        if user_reset == "y":
            print("______________________________________")
            basemath()
        else:
            pass


basemath()
