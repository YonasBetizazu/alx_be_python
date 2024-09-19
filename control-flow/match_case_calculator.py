first_number = int(input("Enter the first number: "))
secound_number = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /):")
if operator=="+":
    print(f"The result is {first_number+secound_number}.")
elif operator=="-":
    print(f"The result is {first_number-secound_number}.")
elif operator=="*":
    print(f"The result is {first_number*secound_number}.")
elif operator=="/":
    if secound_number==int(0):
        print("Cannot divide by zero.")
    else:
        print(f"The result is {first_number/secound_number}.")
