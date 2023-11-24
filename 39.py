#Write a Python program to find the maximum and minimum numbers 
#from the specified decimal numbers. 

def find_max_min(numbers):
    if not numbers:
        return None, None  # Return None for both max and min if the list is empty

    maximum = max(numbers)
    minimum = min(numbers)

    return maximum, minimum

# Example usage
decimal_numbers = [3.14, 2.718, 1.414, 0.0, -1.0, -2.5]
max_value, min_value = find_max_min(decimal_numbers)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

