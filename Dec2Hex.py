import sys

def decimal_to_hex(decimal_value):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    if num == 0:
        return "0"
    
    while num > 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return the hexadecimal value for testing

if __name__ == "__main__":
    if len(sys.argv) != 2:  # Ensure exactly one argument is provided
        print("Error: Please provide exactly one integer as input.")
        sys.exit(1)  # Exit with an error code

    try:
        decimal_value = int(sys.argv[1])  # Convert input to integer
        result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal Output: {result}")
    except ValueError:
        print("Error: Invalid input. Please provide a valid integer.")
        sys.exit(1)  # Exit with an error code
