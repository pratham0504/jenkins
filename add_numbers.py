# add_numbers.py
import sys

def add_numbers(a, b):
    return a + b

def main():
    # Check if there are enough command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 add_numbers.py <num1> <num2>")
        sys.exit(1)
    
    # Input numbers from command-line arguments
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    
    # Add numbers
    result = add_numbers(a, b)
    
    # Print result
    print(f"The sum of {a} and {b} is {result}")

if __name__ == "__main__":
    main()