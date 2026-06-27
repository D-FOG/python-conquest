numbers = [1, -2, 3, 4, -5]


def count_positive_and_negative_numbers(numbers):
    positive_count = 0
    negative_count = 0
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
    return positive_count, negative_count


print("Positive and Negative Count:", count_positive_and_negative_numbers(numbers))
