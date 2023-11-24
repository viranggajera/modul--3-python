#Write a Python program to find the second smallest number in a list. 

def second_smallest_number(input_list):
    unique_sorted_list = sorted(set(input_list))
    return unique_sorted_list[1]

# Example usage:
my_list = [5, 2, 8, 1, 7, 3, 2, 1]
second_smallest = second_smallest_number(my_list)

print("Original List:", my_list)
print("Second Smallest Number (considering repeated elements):", second_smallest)
