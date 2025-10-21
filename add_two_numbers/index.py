# Write a function add(a, b) that returns the sum. Call it with 2 and 5.

def add(a: int, b: int) -> int:
    return a + b

def main() -> None:
    result = add(2, 5)
    print(f"The sum of 2 and 5 is: {result}")

if __name__ == "__main__":
    main()