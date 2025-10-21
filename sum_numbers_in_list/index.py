# Given nums = [1, 2, 3, 4], calculate and print the total.

def sum_numbers(nums: list[int]) -> int:
    return sum(nums)


def main() -> None:
    numbers = [1, 2, 3, 4]
    total = sum_numbers(numbers)
    print(f"The sum is: {total}")


if __name__ == "__main__":
    main()