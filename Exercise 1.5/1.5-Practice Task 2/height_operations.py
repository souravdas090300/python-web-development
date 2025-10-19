# Practice Task 2: Operator Overloading - Subtraction
# Exercise 1.5 - Object-Oriented Programming

class Height(object):
    """
    A class to represent height in feet and inches.
    Supports subtraction operation.
    """
    
    def __init__(self, feet, inches):
        """Initialize Height with feet and inches."""
        self.feet = feet
        self.inches = inches
    
    def __str__(self):
        """Return string representation of Height."""
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output
    
    def __sub__(self, other):
        """
        Subtract two Height objects.
        
        Args:
            other: Another Height object to subtract
            
        Returns:
            Height: New Height object with the difference
        """
        # Convert both heights to inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        
        # Subtract them
        total_height_inches = height_A_inches - height_B_inches
        
        # Convert back to feet and inches
        output_feet = total_height_inches // 12  # Integer division
        output_inches = total_height_inches % 12  # Remainder
        
        # Return new Height object
        return Height(output_feet, output_inches)


# Main code
print("=" * 50)
print("Height Subtraction - Practice Task 2")
print("=" * 50)

# Create two Height objects
height_A = Height(5, 10)  # 5 feet 10 inches
height_B = Height(3, 9)   # 3 feet 9 inches

# Display original heights
print("\nOriginal Heights:")
print("-" * 50)
print("Height A:", height_A)
print("Height B:", height_B)

# Perform subtraction
print("\nPerforming Subtraction (A - B):")
print("-" * 50)
height_difference = height_A - height_B

# Display result
print("Result:", height_difference)
print("=" * 50)
