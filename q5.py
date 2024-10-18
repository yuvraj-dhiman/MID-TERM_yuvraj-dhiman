#!/usr/bin/env python3

def sum_of_digits(number):
    total = 0
    for digit in str(number):  
        total += int(digit)  
    return total

if __name__ == '__main__':
    user_input = int(input("Enter an integer: "))  # Get input from user
    result = sum_of_digits(user_input)  # Call the function
    print(f"The sum of the digits is: {result}")  # Print the result

