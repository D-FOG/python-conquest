numbers = [8, 3, 15, 6, 2]


def smallest_number(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


print("Smallest number:", smallest_number(numbers))
