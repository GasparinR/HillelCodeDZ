while True:
    user_number = int(input("Enter the first number: "))
    print("Reference for choice: +, -, *, /")
    user_operator = input("Enter your math operation: ")
    user_number2 = int(input("Enter second number: "))

    if user_operator == "+":
        user_result = user_number + user_number2
    elif user_operator == "-":
        user_result = user_number - user_number2
    elif user_operator == "*":
        user_result = user_number * user_number2
    elif user_operator == "/":
        user_result = user_number / user_number2
    else:
        print("Operation Error! Try again.")
        continue

    print("Result:", user_result)
    print("______________________________________")
    user_reset = input("Do a new operation? Write 'y' if yes or something else if no: ")

    if user_reset.lower() != 'y':
        break
    print("______________________________________")
