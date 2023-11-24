#Write a Python program to generate and print a list of first and last 5 
#elements where the values are square of numbers between 1 and 30.

def generate_squares_list(start, end):
    squares_list = [x ** 2 for x in range(start, end + 1)]
    return squares_list

# Generate the squares list for numbers between 1 and 30
squares_list = generate_squares_list(1, 30)

# Print the first and last 5 elements
print("First 5 elements:", squares_list[:5])
print("Last 5 elements:", squares_list[-5:])
