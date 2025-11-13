# input() function in Python is used to take input from the user via the console.
# The input() function reads a line from input, converts it into a string (stripping a trailing newline), and returns it.

# Taking user input for different data types
firstName = input("Enter your name: ")          # String input
age = int(input("Enter your age: "))            # Integer input
height = float(input("Enter your height in feet: "))  # Float input
is_student = input("Are you a student? (yes/no): ").strip().lower() == 'yes'  # Boolean input
# Note: The boolean input is derived from a string comparison
# Displaying the user input
print(f"Name: {firstName}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# Note: When using input(), the data is always received as a string.
# .strip() is used to remove any leading/trailing whitespace.
# .lower() is used to convert the input to lowercase for easier comparison.
