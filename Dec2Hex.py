import sys

def decimal_to_hex(decimal_value):
    # Check if the input is a valid integer
    if not isinstance(decimal_value, int):
        raise ValueError("Input must be an integer")

    # Handle negative numbers by keeping track of the sign
    is_negative = decimal_value < 0
    num = abs(decimal_value)  # Work with the absolute value for conversion

    print(f"Converting the Decimal Value {decimal_value} to Hex...")

    if num == 0:
        return "0"  # Special case for 0
    
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    
    # Convert the decimal number to hexadecimal using manual division
    while num > 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    
    # Return the result with a negative sign if the number was negative
    return f"-{hexadecimal}" if is_negative else hexadecimal


if __name__ == "__main__":
    if len(sys.argv) != 2:  # Ensure exactly one argument is provided
        print("Error: Please provide exactly one positive integer as input.")
        sys.exit(1)  # Exit with an error code

    try:
        decimal_value = int(sys.argv[1])  # Convert input to integer

        if decimal_value < 0:
            print("Error: Negative numbers are not supported. Please enter a positive integer.")
            sys.exit(1)

        result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal Output: {result}")

    except ValueError:
        print("Error: Invalid input. Please provide a valid positive integer.")
        sys.exit(1)  # Exit with an error code
