import multiprocessing


def compute(my_list, result_queue):
    new_value = []
    for l in my_list:
        new_value.append(l**2)
    result_queue.put(new_value)


def main():
    simple_list = [i for i in range(1, 11)]
    print(simple_list)

    l1 = simple_list[:(len(simple_list) // 2)]
    print("l1: ", l1)

    l2 = simple_list[(len(simple_list) // 2):]
    print("l2: ", l2)

    result_queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=compute, args=(l1, result_queue))
    process2 = multiprocessing.Process(target=compute, args=(l2, result_queue))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print("Results: ", results)


if __name__ == "__main__":
    main()