# Given person = ("John", 25), unpack it into name and age, then print both.

def main() -> None:
    person = ("John", 25)
    name, age = person
    print(f"Name: {name}, Age: {age}")

if __name__ == "__main__":
    main()