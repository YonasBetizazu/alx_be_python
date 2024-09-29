FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def main():
    global temperature
    temperature = float(input("Enter the temperature to convert: "))
    celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    
    if celsius_or_fahrenheit == 'c':
        convert_to_fahrenheit(temperature)
    elif celsius_or_fahrenheit == "f":
        convert_to_celsius(temperature)
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} F is {result:.2f} C")

def convert_to_fahrenheit(celsius):
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius} C is {result:.2f} F")

if __name__ == "__main__":
    main()
