user_number = int(input("enter the first number:"))
print(" reference for choice: 1 - +, 2 - '-', 3 - *, 4 - /")
user_operator = int(input("enter your math operation:"))
user_number2 = int(input("enter second number:"))

if user_operator == 1:
    user_result = user_number + user_number2
    print(user_result)
elif user_operator == 2:
    user_result = user_number - user_number2
    print(user_result)
elif user_operator == 3:
    if user_number == 0:
        print("The divisor is 0, the answer will always be 0. Try again!")
    elif user_number2 == 0:
        print("The divisor is 0, the answer will always be 0. Try again!")
    else:
        user_result = user_number * user_number2
        print(user_result)

elif user_operator == 4:
    if user_number == 0:
        print("The divisor is 0, the answer will always be 0. Try again!")
    elif user_number2 == 0:
        print("The divisor is 0, the answer will always be 0. Try again!")
    else:
        user_result = user_number / user_number2
        print(user_result)
else:
    print("Operation Error! Try again.")
