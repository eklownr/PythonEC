import threading
import multiprocessing
import time

counter = 0
counter_lock = threading.Lock()
num_threads = 10
sleep_timer = 0.2


def increment_counter_with_lock():
    global counter
    with counter_lock:
        current_value = counter
        time.sleep(sleep_timer)
        counter = current_value + 1


def increment_counter_without_lock():
    global counter
    current_value = counter
    time.sleep(sleep_timer)
    counter = current_value + 1


def multithreading_example():
    global counter
    counter = 0
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=increment_counter_with_lock)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Counter (with lock):", counter)


def multithreading_race_condition_example():
    global counter
    counter = 0
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=increment_counter_without_lock)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Counter (without lock, race condition):", counter)


def square_numbers(numbers, result_queue):
    for num in numbers:
        result_queue.put(num * num)


def multiprocessing_example():
    numbers = [1, 2, 3, 4, 5]

    result_queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(
        target=square_numbers, args=(numbers[: len(numbers) // 2], result_queue)
    )
    process2 = multiprocessing.Process(
        target=square_numbers, args=(numbers[len(numbers) // 2 :], result_queue)
    )

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print("Original numbers:", numbers)
    print("Squared numbers:", results)


if __name__ == "__main__":
    multithreading_example()
    multithreading_race_condition_example()
    multiprocessing_example()
