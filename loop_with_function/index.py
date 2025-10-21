# List of names with function
# Write a function that takes a list of names and prints: "Hello, <name>!" for each.

from typing import List

def greet_names(names: List[str]) -> None:
    for name in names:
        print(f"Hello, {name}!")

def main() -> None:
    names = ["Alice", "Bob", "Charlie"]
    greet_names(names)

if __name__ == "__main__":
    main()