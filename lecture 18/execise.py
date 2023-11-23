"""
Todays Exercise:

1, Define a function, let's call it compute_operation, 
that takes a list of numbers and performs a mathematical operation on each number. 
The specific operation can be something like squaring, cubing, 
or finding the square root.

2, Create a list of numbers (e.g., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).

3, Split the list into two or more subsets.

4, Create a multiprocessing process for each subset of the list, 
passing the subset and the result queue to each process.

5, In each process, call the compute_operation function on 
the subset of numbers and put the results into the result queue.

6, Collect the results from the result queue in the main process 
and print the final results.

Effectively the end result should be a more optimized 
and code leaner solution than the one we did in the lecture!

"""

def compute(my_list):
    new_value = []
    for l in my_list:
        new_value.append(l**2)
    return new_value


def main():
    simple_list = [i for i in range(1,11)]
    print(simple_list)

    l1 = simple_list[:(len(simple_list) // 2)]
    print("l1: ", l1)


    l2 = simple_list[(len(simple_list) // 2):]
    print("l2: ", l2)


if __name__ == "__main__":
    main()        