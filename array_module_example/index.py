# Import the array module. Create an array of 5 integers. Print the first and last.

import array

def main() -> None:
    arr = array.array('i', [10, 20, 30, 40, 50])
    print(f"First element: {arr[0]}")
    print(f"Last element: {arr[-1]}")

if __name__ == "__main__":
    main()