numbers = [1, 2, 5, 10, 9, 15, 16]


def square(x):
    return x**2


square_numbers = list(map(square, numbers))
print(square_numbers)


def my_map(func, my_iterable):
    """This function showcases how map functions ish"""
    for e in my_iterable:
        new_element = func(e)
        print(new_element)


# my_map(square, numbers)

cube_numbers = list(map(lambda x: x**3, numbers))
print(cube_numbers)

# ------------------- End of MAP
# ------------------- Now starts Filter

even_numbers = list(filter(lambda element: element % 5 == 0, numbers))
print(even_numbers)


# ------------------- End of FILTER
# ------------------- Now starts Reduce

from functools import reduce

letters = ["a", "b", "cdeerfe"]
sum_numbers = reduce(lambda x, y: x * y, numbers)
conc_letters = reduce(lambda x, y: x + y, letters)

print(sum_numbers)
print(conc_letters)

# my_var = str("a" + 5)
# print(my_var)

print(sum([5, 12, 13]))
