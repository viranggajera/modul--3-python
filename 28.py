#Write a Python program to remove an empty tuple(s) from a list of tuples.
# Function to remove empty tuples from a list of tuples
def remove_empty_tuples(tuple_list):
    non_empty_tuples = [tpl for tpl in tuple_list if tpl]
    return non_empty_tuples

# Example usage:
list_of_tuples = [(1, 2, 3), (), (4, 5), (), (6, 7, 8), ()]

# Remove empty tuples from the list
result_list = remove_empty_tuples(list_of_tuples)

# Print the original and modified lists
print("Original List of Tuples:", list_of_tuples)
print("List of Tuples without Empty Tuples:", result_list)
