#Write a Python program to select an item randomly from a list. 

import random

def select_random_item(input_list):
    return random.choice(input_list)

# Example usage:
my_list = [1, 2, 3, 4, 5]
random_item = select_random_item(my_list)

print("Original List:", my_list)
print("Randomly Selected Item:", random_item)
