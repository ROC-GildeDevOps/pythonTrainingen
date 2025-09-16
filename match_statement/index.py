# Ask the user for a number (1–7). Use match to print the day name.

def get_day_of_week(number: int) -> str:
    match number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Number must be between 1 and 7."

def main() -> None:
    try:
        number = int(input("Enter a number (1-7): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print(get_day_of_week(number))

if __name__ == "__main__":
    main()
