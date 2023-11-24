#Write a Python program to unzip a list of tuples into individual lists. 

# Function to unzip a list of tuples into individual lists
def unzip_tuples(tuple_list):
    # Using the zip function to unzip the tuples
    unzipped_lists = list(zip(*tuple_list))
    
    return unzipped_lists

# Example usage:
list_of_tuples = [(1, 2, 3), ('a', 'b', 'c'), (4, 5, 6)]

# Unzip the list of tuples
unzipped_result = unzip_tuples(list_of_tuples)

# Print the original list of tuples and the unzipped result
print("Original List of Tuples:", list_of_tuples)
print("Unzipped Result:", unzipped_result)
