from functools import reduce

numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


squared_numbers2 = list(map(square, numbers))
squared_numbers = list(map(lambda x: x**2, numbers))
# Result: squared_numbers = [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# Result: even_numbers = [2, 4]

resulting_sum = reduce(lambda x, y: x + y, numbers)
# Result: result = 15 (1 + 2 + 3 + 4 + 5)

print(squared_numbers)
print(squared_numbers2)
print(even_numbers)
print(resulting_sum)

my_string = " Hello, world! "
stripped_string = my_string.strip() 

print(stripped_string) 
