# Ask for a number. Handle the error if the user enters text instead of a number.

def ask() -> int:
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit(1)

def main() -> None:
    number = ask()
    print(f"You entered the number: {number}")

if __name__ == "__main__":
    main()