numbers = [2, 5, 8, 9, 10]


def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


print("Count of even numbers:", count_even_numbers(numbers))
