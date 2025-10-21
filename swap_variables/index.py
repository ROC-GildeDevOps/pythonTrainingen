# Create two variables a = 5, b = 10. Swap the values without using a third variable.


def swap(a: int, b: int) -> tuple[int, int]:
    return b, a

def main():
    a = 5
    b = 10

    print(f"Before: A = {a}, B = {b}")

    a, b = swap(a, b)

    print(f"After: A = {a}, B = {b}")


if __name__ == "__main__":
    main()
