#Write a Python function to get the largest number, smallest num and sum 
#of all from a list. 


def get_list_stats(numbers):
    if not numbers:
        return None  # Return None for an empty list

    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)

    return largest, smallest, total_sum

# Example usage:
my_list = [2, 33, 222, 14, 25]
result = get_list_stats(my_list)

print("Largest number:", result[0])
print("Smallest number:", result[1])
print("Sum of all numbers:", result[2])
