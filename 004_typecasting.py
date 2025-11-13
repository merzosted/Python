# Typecasting -> The process of converting a variable from one data type to another data type is called typecasting.
# In Python, you can use built-in functions like int(), float(), str(), and bool() to perform typecasting.

name = "Alice"          # String variable
age = 25
height = 5.7           # Float variable
is_student = False     # Boolean variable

#  How to check the type of a variable

print("Before Typecasting:")
print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Is Student:", is_student, "Type:", type(is_student))

# Typecasting
age_as_string = str(age)               # Converting integer to string
height_as_integer = int(height)        # Converting float to integer    
is_student_as_integer = int(is_student) # Converting boolean to integer
name_as_boolean = bool(name)           # Converting string to boolean
# Note: Non-empty strings convert to True, empty strings convert to False
print("\nAfter Typecasting:")
print("Age as String:", age_as_string, "Type:", type(age_as_string))
print("Height as Integer:", height_as_integer, "Type:", type(height_as_integer))
print("Is Student as Integer:", is_student_as_integer, "Type:", type(is_student_as_integer))
print("Name as Boolean:", name_as_boolean, "Type:", type(name_as_boolean))