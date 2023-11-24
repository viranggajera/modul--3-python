#Write a Python function that takes two lists and returns true if they have 
#at least one common member.


def have_common_member_loop(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]

if have_common_member_loop(list_a, list_b):
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")
