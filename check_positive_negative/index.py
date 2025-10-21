# Write a function that checks if a number is positive, negative, or zero.

def ask() -> float:
    try:
        return float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        exit(1)

def check_positive_negative(number: float) -> str:
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    
def main() -> None:
    number = ask()
    result = check_positive_negative(number)
    print(f"The number is: {result}")

if __name__ == "__main__":
    main()