#Write a Python program to returns sum of all divisors of a number

def sum_of_divisors(number):
    divisor_sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            divisor_sum += i

    return divisor_sum

# Example usage
num = 12
result = sum_of_divisors(num)

print(f"The sum of divisors of {num} is: {result}")
