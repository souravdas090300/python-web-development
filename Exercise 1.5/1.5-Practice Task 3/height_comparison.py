# Practice Task 3: Comparison Operators
# Exercise 1.5 - Object-Oriented Programming

class Height(object):
    """
    A class to represent height in feet and inches.
    Supports comparison operations.
    """
    
    def __init__(self, feet, inches):
        """Initialize Height with feet and inches."""
        self.feet = feet
        self.inches = inches
    
    def __str__(self):
        """Return string representation of Height."""
        return f"{self.feet} feet, {self.inches} inches"
    
    # Existing comparison operators (from the tutorial)
    def __lt__(self, other):
        """Less than operator (<)"""
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A < height_inches_B
    
    def __le__(self, other):
        """Less than or equal to operator (<=)"""
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A <= height_inches_B
    
    def __eq__(self, other):
        """Equal to operator (==)"""
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A == height_inches_B
    
    # NEW: Operators you need to implement
    def __gt__(self, other):
        """Greater than operator (>)"""
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B
    
    def __ge__(self, other):
        """Greater than or equal to operator (>=)"""
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B
    
    def __ne__(self, other):
        """Not equal to operator (!=)"""
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B


# Main code - Testing comparison operators
print("=" * 60)
print("Height Comparison Operators - Practice Task 3")
print("=" * 60)

# Test Case 1: Greater than (>)
print("\nTest Case 1: Height(4, 6) > Height(4, 5)")
print("-" * 60)
result1 = Height(4, 6) > Height(4, 5)
print(f"Result: {result1}")
print(f"Expected: True")
print(f"Status: {'✅ PASS' if result1 == True else '❌ FAIL'}")

# Test Case 2: Greater than or equal to (>=)
print("\nTest Case 2: Height(4, 5) >= Height(4, 5)")
print("-" * 60)
result2 = Height(4, 5) >= Height(4, 5)
print(f"Result: {result2}")
print(f"Expected: True")
print(f"Status: {'✅ PASS' if result2 == True else '❌ FAIL'}")

# Test Case 3: Not equal to (!=)
print("\nTest Case 3: Height(5, 9) != Height(5, 10)")
print("-" * 60)
result3 = Height(5, 9) != Height(5, 10)
print(f"Result: {result3}")
print(f"Expected: True")
print(f"Status: {'✅ PASS' if result3 == True else '❌ FAIL'}")

# Bonus: Show all comparison operators working
print("\n" + "=" * 60)
print("Bonus: All Comparison Operators Demo")
print("=" * 60)

h1 = Height(5, 10)
h2 = Height(4, 8)

print(f"\nh1 = {h1}")
print(f"h2 = {h2}\n")

print(f"h1 < h2  : {h1 < h2}")
print(f"h1 <= h2 : {h1 <= h2}")
print(f"h1 == h2 : {h1 == h2}")
print(f"h1 != h2 : {h1 != h2}")
print(f"h1 > h2  : {h1 > h2}")
print(f"h1 >= h2 : {h1 >= h2}")

print("\n" + "=" * 60)
print("All tests completed!")
print("=" * 60)
