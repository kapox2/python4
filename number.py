# Procedural Programming Example
def calculate_area(radius):
    return 3.14 * radius * radius

def calculate_circumference(radius):
    return 2 * 3.14 * radius

# Calling functions
radius = 5
print("Area:", calculate_area(radius))
print("Circumference:", calculate_circumference(radius))



class Rectangle:
    def __init__(self, length, width):
        self.length = length  # Instance variable for length
        self.width = width    # Instance variable for width

    def calculate_area(self):
        # Area of rectangle = length * width
        return self.length * self.width

    def calculate_circumference(self):
        # Perimeter of rectangle = 2 * (length + width)
        return 2 * (self.length + self.width)

# Creating an instance of the Rectangle class with length 5 and width 3
my_rectangle = Rectangle(5, 3)

# Calling the methods to calculate area and circumference
print(f"Area of Rectangle: {my_rectangle.calculate_area()}")  # Output: 15
print(f"Circumference of Rectangle: {my_rectangle.calculate_circumference()}")  # Output: 16

