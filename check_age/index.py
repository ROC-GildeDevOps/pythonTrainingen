# Ask for age input. Print "Child" if < 12, "Teen" if 12–17, "Adult" if 18+.

def clarify_age_group(age: int) -> str:
    if age < 0:
        return "Invalid age"
    elif age < 12:
        return "Child"
    elif age <= 17:
        return "Teen"
    else:
        return "Adult"

def main() -> None:
    try:
        age = int(input("Enter your age (non-negative integer): "))
        if age < 0:
            print("Age cannot be negative.")
        else:
            print(clarify_age_group(age))
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
