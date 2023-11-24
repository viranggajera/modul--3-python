#Write a Python program to remove duplicates from a list.


def remove_duplicates_order_preserved(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates_order_preserved(original_list)

print("Original List:", original_list)
print("List after removing duplicates with order preserved:", result_list)
