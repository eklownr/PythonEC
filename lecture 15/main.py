import time

numbers = list(range(1, 1000001))

start_time = time.time()
squares_loop = []
for num in numbers:
    squares_loop.append(num**2)
end_time = time.time()

print("Time taken for traditional loop: {:.6f} seconds".format(end_time - start_time))

start_time = time.time()
squares_comprehension = [num**2 for num in numbers]
end_time = time.time()

print("Time taken for list comprehension: {:.6f} seconds".format(end_time - start_time))

assert squares_loop == squares_comprehension
