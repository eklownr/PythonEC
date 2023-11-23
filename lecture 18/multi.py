import multiprocessing
import concurrent.futures
import time


def square(numbers, queue):
    for num in numbers:
        queue.put(num**2)


def multiprocessing_example():
    my_list = [1, 3, 8, 5, 10, 11, 161, 8]

    result_queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(
        target=square, args=(my_list[: len(my_list) // 2], result_queue)
    )
    process2 = multiprocessing.Process(
        target=square, args=(my_list[len(my_list) // 2 :], result_queue)
    )

    process2.start()
    process1.start()

    process2.join()
    process1.join()

    results = []

    print(dir(result_queue))

    while not result_queue.empty():
        results.append(result_queue.get())

    print(results)


def task(name):
    # print("Task started")
    time.sleep(0.5)
    # print("task completed")
    return f"task {name} completed"


def multithreading_example():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(task, i) for i in range(20)]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)


def main():
    # multiprocessing_example()
    multithreading_example()


if __name__ == "__main__":
    main()
