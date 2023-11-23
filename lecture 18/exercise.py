"""
Todays Exercise:

- Define a function, let's call it compute_operation, that takes a list of numbers and performs a mathematical operation on each number. The specific operation can be something like squaring, cubing, or finding the square root.

- Create a list of numbers (e.g., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).

- Split the list into two or more subsets.

- Create a multiprocessing process for each subset of the list, passing the subset and the result queue to each process.

- In each process, call the compute_operation function on the subset of numbers and put the results into the result queue.

- Collect the results from the result queue in the main process and print the final results.

Effectively the end result should be a more optimized and code leaner solution than the one we did in the lecture!

"""
