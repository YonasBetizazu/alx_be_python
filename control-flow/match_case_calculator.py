first_number = int(input("Enter the first number: "))
secound_number = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")


match operation:
    case "+":
        print(f"The result is {first_number+secound_number}.")
    case "-":
        print(f"The result is {first_number-secound_number}.")
    case "*":
        print(f"The result is {first_number*secound_number}.")
    case("/"):
         if secound_number==0:
             print("Cannot divide by zero.")
         else: 
             print(f"The result is {first_number/secound_number}.")
