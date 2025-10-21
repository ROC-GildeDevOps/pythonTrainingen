# Ask the user for two numbers. Divide them. Handle division by zero with try/except.

def ask() -> tuple[int, int]:
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter integers.")
        exit(1)

def safe_divide(numerator: int, denominator: int) -> float:
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        exit(1)

def main() -> None:
    numerator, denominator = ask()
    result = safe_divide(numerator, denominator)
    print(f"The result of {numerator} divided by {denominator} is {result}")

if __name__ == "__main__":
    main()