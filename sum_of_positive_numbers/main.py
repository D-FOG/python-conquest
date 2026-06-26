mixed_numbers = [1, -2, 3, 4, -5]


def sum_of_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total


print("Sum of positive numbers:", sum_of_positive_numbers(mixed_numbers))
