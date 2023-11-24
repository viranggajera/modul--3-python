#Write a Python program to count the number of strings where the string 
#length is 2 or more and the first and last character are same from a given 
#list of strings. 

def count_strings_with_same_ends(strings):
    count = 0

    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1

    return count

# Example usage:
my_strings = ["level", "python", "deed", "hello", "radar"]
result = count_strings_with_same_ends(my_strings)

print("Number of strings with the same first and last character:", result)
