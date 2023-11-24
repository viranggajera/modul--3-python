#Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary. 
#Sample data: {'1': ['a','b'], '2': ['c','d']} 
#Expected Output: 
#ac ad bc bd

from itertools import product

# Sample data
data_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

# Generate all combinations of letters
combinations = [''.join(combination) for combination in product(*data_dict.values())]

# Print the result
print("All Combinations of Letters:", ' '.join(combinations))
