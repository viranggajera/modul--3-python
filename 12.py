#Write a Python program to convert a list of characters into a string. 
def list_to_string(char_list):
    return ''.join(char_list)

# Example usage:
char_list = ['a', 'b', 'c', 'd', 'e']
result_string = list_to_string(char_list)

print("List of Characters:", char_list)
print("String Result:", result_string)
