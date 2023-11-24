#How will you compare two lists?

list1 = [1, 2, 3]
list2 = [3, 2, 1]

if sorted(list1) == sorted(list2):
    print("The lists are equal.")
else:
    print("The lists are not equal.")
