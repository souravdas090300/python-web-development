"""Simple script for Exercise 1.1

This script reads two integers from the user, adds them and prints the result.
It also exposes an `add(a, b)` function so the behavior can be tested programmatically.
"""

from typing import Any


def add(a: Any, b: Any) -> Any:
    """Return the sum of a and b.

    This keeps behavior permissive (works with ints, floats, and other +-compatible types).
    """
    return a + b


def read_int(prompt: str) -> int:
    """Read an integer from input with a prompt. Keeps asking until a valid integer is given."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number (integer).")


def main() -> None:
    """Main function that follows mentor instructions exactly."""
    # Read first number and store in variable a
    a = int(input("Enter first number: "))
    
    # Read second number and store in variable b
    b = int(input("Enter second number: "))
    
    # Add a and b, store result in variable c
    c = a + b
    
    # Print the value of c
    print(c)


if __name__ == "__main__":
    main()


