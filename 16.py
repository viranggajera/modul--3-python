#Write a Python program to check whether a list contains a sub list

def contains_sublist(main_list, sublist):
    # Check if sublist is empty
    if not sublist:
        return True

    # Iterate through the main list
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i + len(sublist)] == sublist:
            return True

    return False

# Example usage:
main_list = [1, 2, 3, 4, 5, 6, 7]
sub_list1 = [3, 4, 5]
sub_list2 = [8, 9, 10]

if contains_sublist(main_list, sub_list1):
    print("The main list contains sub_list1.")
else:
    print("The main list does not contain sub_list1.")

if contains_sublist(main_list, sub_list2):
    print("The main list contains sub_list2.")
else:
    print("The main list does not contain sub_list2.")
