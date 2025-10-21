# Ask for a number, print its multiplication table from 1 to 10.

def ask() -> int:
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit(1)

def print_multiplication_table(number: int) -> None:
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def main() -> None:
    number = ask()
    print_multiplication_table(number)

if __name__ == "__main__":
    main()

