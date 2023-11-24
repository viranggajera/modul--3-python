#Write a Python program to convert a tuple to a string.

# Creating a tuple with numbers
number_tuple = (1, 2, 3, 4, 5)

# Converting the tuple to a string representation
result_string = ''.join(str(item) for item in number_tuple)

# Printing the result
print("Result String:", result_string)
