"""Quick test runner for Exercise 1.1

Runs a small test against the add function from add.py.
Simplified as per mentor recommendation.
"""
from add import add


def main():
    """Test the add function with various inputs."""
    assert add(2, 3) == 5, "add(2,3) should equal 5"
    assert add(-1, 1) == 0, "add(-1,1) should equal 0"
    assert add(0, 0) == 0, "add(0,0) should equal 0"
    assert add(100, 200) == 300, "add(100,200) should equal 300"
    print("All tests passed.")


if __name__ == "__main__":
    main()
