#Write a Python program to replace last value of tuples in a list.
# Function to replace the last value of tuples in a list
def replace_last_value(tuples_list, new_value):
    modified_list = [tuple(lst[:-1] + (new_value,)) for lst in tuples_list]
    return modified_list

# Example usage:
list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_last_value = 99

# Replace the last value in each tuple
modified_list = replace_last_value(list_of_tuples, new_last_value)

# Print the original and modified lists
print("Original List of Tuples:", list_of_tuples)
print("Modified List of Tuples:", modified_list)
