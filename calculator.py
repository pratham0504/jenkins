# calculator.py
import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    # Check if there are enough command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python3 calculator.py <operation> <num1> <num2>")
        sys.exit(1)
    
    # Input operation and numbers from command-line arguments
    operation = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    
    # Perform the chosen operation
    if operation == 'add':
        result = add(a, b)
    elif operation == 'subtract':
        result = subtract(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    elif operation == 'divide':
        result = divide(a, b)
    else:
        print("Error: Unsupported operation. Use add, subtract, multiply, or divide.")
        sys.exit(1)
    
    # Print result
    print(f"The result of {operation} {a} and {b} is {result}")

if __name__ == "__main__":
    main()