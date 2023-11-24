#Write a Python program to check whether an element exists within a 
#tuple. 


# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Checking if an element exists in the tuple
element_to_check = 3

if element_to_check in my_tuple:
    print(f"{element_to_check} exists in the tuple.")
else:
    print(f"{element_to_check} does not exist in the tuple.")
