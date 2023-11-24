#Write a Python function to check whether a number is in a given range


def is_in_range(number, start, end):
    """
    Check if the given number is in the inclusive range [start, end].
    
    Parameters:
    - number: The number to check.
    - start: The start of the range.
    - end: The end of the range.
    
    Returns:
    - True if the number is in the range, False otherwise.
    """
    return start <= number <= end

# Example usage
number_to_check = 15
start_range = 10
end_range = 20

if is_in_range(number_to_check, start_range, end_range):
    print(f"{number_to_check} is in the range [{start_range}, {end_range}]")
else:
    print(f"{number_to_check} is not in the range [{start_range}, {end_range}]")
