numbers = [2, 4, 6, 8]


def average_number(numbers):
    count = len(numbers)
    total = 0
    for num in numbers:
        total += num
        average = total / count
    return average


print("Average number:", average_number(numbers))

# update do this instead


def average(numbers):
    count = len(numbers)
    total = 0
    for num in numbers:
        total += num
    average = total / count
    return average


print("Average number:", average(numbers))
