# Ask the user for a number. Print "Even" if it's even, else print "Odd".

def ask() -> int:
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit(1)

def isEven(number: int) -> bool:
    return number % 2 == 0

def main() -> None:
    number = ask()
    print("Even" if isEven(number) else "Odd")

if __name__ == "__main__":
    main()
