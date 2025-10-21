# Create a tuple with your birth year, month, and day. Print each value.

def get_birthdate() -> tuple[int, int, int]:
    return (14, 3, 2007)

def print_birthdate(birthdate: tuple[int, int, int]) -> None:
    day, month, year = birthdate
    print(f"Day: {day}")
    print(f"Month: {month}")
    print(f"Year: {year}")

def main() -> None:
    birthdate = get_birthdate()
    print_birthdate(birthdate)

if __name__ == "__main__":
    main()