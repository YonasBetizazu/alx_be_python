first_number = int(input("Enter the first number: "))
secound_number = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")
if operation== "+":
    print(f"The result is {first_number+secound_number}.")
elif operation== "-":
    print(f"The result is {first_number-secound_number}.")
elif operation== "*":
    print(f"The result is {first_number*secound_number}.")
elif operation== "/":
    if secound_number==int(0):
        print("Cannot divide by zero.")
    else:
        print(f"The result is {first_number/secound_number}.")
