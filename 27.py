#Write a Python program to find the repeated items of a tuple.

# Function to find repeated items in a tuple
def find_repeated_items(my_tuple):
    element_count = {}
    repeated_items = set()

    for item in my_tuple:
        if item in element_count:
            element_count[item] += 1
            repeated_items.add(item)
        else:
            element_count[item] = 1

    return repeated_items

# Example usage:
my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 7)

# Find repeated items in the tuple
repeated_items = find_repeated_items(my_tuple)

# Print the result
print("Original Tuple:", my_tuple)
print("Repeated Items:", repeated_items)

