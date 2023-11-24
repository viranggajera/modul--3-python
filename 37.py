#How can you pick a random item from a range?

import random

my_list = [1, 2, 3, 4, 5]
my_tuple = ('apple', 'banana', 'orange', 'grape')

# Pick a random item from a list
random_item_from_list = random.choice(my_list)
print("Random item from list:", random_item_from_list)

# Pick a random item from a tuple
random_item_from_tuple = random.choice(my_tuple)
print("Random item from tuple:", random_item_from_tuple)
