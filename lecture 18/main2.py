import threading
import time

my_lock = threading.Lock()
sleep_timer = 0.2
lock_counter = 0
without_lock_counter = 0
amount_of_threads = 10


def increment_counter_without_lock():
    global without_lock_counter
    # NOTERA: ALLA TRÅDARNA KOMMER FÅ SAMMA CURRENT_VALUE FÖR ALLA ÄR TYP LIKA SNABBA
    current_value = without_lock_counter
    time.sleep(sleep_timer)
    without_lock_counter = current_value + 1


def increment_counter_with_lock():
    global lock_counter

    # Tänk att with statement gör my_lock.open() och när din kod är klar gör den my_lock.close()
    with my_lock:
        current_value = lock_counter
        time.sleep(sleep_timer)
        lock_counter = current_value + 1


def multithread_counter():
    my_threads = [
        threading.Thread(target=increment_counter_without_lock)
        for _ in range(amount_of_threads)
    ]
    my_threads2 = [
        threading.Thread(target=increment_counter_with_lock)
        for _ in range(amount_of_threads)
    ]

    for thread_index in range(amount_of_threads):
        my_threads[thread_index].start()
        my_threads2[thread_index].start()

    for thread_index in range(amount_of_threads):
        my_threads[thread_index].join()
        my_threads2[thread_index].join()

    print("The counter with a lock is: ", lock_counter)
    print("The counter without a lock is: ", without_lock_counter)


def main():
    multithread_counter()


if __name__ == "__main__":
    main()
