numbers = [8, 3, 15, 6, 2]
# numbers = [-8, -3, -15, -6, -2]


def largest_number(numbers):
    maximum = 0
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


print("Largest number:", largest_number(numbers))

# above is correct however if all numbers are negative [-8, -3, -15, -6, -2], the function will return 0 instead of the largest negative number. To fix this, we can initialize `maximum` to the first element of the list instead of 0. Here's the corrected code:
# maximum = 0 assumes there will always be a number greater than or equals zero in the list


def largest_number(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


print("Largest number:", largest_number(numbers))
