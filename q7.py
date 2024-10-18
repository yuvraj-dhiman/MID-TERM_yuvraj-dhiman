#!/usr/bin/env python3

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1  # Initialize factorial
    for i in range(1, n + 1):  # Loop from 1 to n
        factorial *= i  # Multiply to get factorial
    return factorial

if __name__ == '__main__':
    user_input = int(input("Enter a positive integer: "))  # Get input from user
    result = calculate_factorial(user_input)  # Call the function
    print(f"Factorial  is: {result}")  # Print the result

