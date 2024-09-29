import datetime
from datetime import timedelta


def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")

def calculate_future_date(days):
    # Calculate the future date
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    # Format the future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    
    # Get user input and convert to integer
    day = int(input("Enter the number of days to add to the current date: "))
    
    # Call the function to calculate the future date
    calculate_future_date(day)

if __name__ == "__main__":
    main()
