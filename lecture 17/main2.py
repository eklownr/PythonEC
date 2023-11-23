import threading
import time

s1 = time.time()


def count_numbers():
    s2 = time.time()
    total_sum = 0
    for i in range(1000):
        total_sum += i

    e2 = time.time()
    print("thread 1 exectued, it took: ", e2 - s2, "time")


def print_letters():
    counts = 0
    for letter in "ABCDE":
        time.sleep(1)
        print(letter)


def print_numbers():
    for number in range(5):
        time.sleep(1)
        print(number)


total_sum = 0
I_RANGE = 10000000


def sum_my_numbers():
    global total_sum
    for i in range(I_RANGE):
        total_sum += 1


""" thread1 = threading.Thread(target=print_letters)
thread2 = threading.Thread(target=print_numbers) """
thread3 = threading.Thread(target=sum_my_numbers)
thread4 = threading.Thread(target=sum_my_numbers)
thread4.start()
thread4.join()
thread3.start()
thread3.join()


print(f"Expected sum is {2*i_range}")
print(f"Outputted sum by threads is {total_sum}")


""" 
thread1.start()
thread2.start()

thread1.join()
thread2.join() """


# thread1 = threading.Thread(target=count_numbers)
# thread1.start()
# e1 = time.time()
# print("main programme stopped executing, it took: ", e1 - s1, "time")
# thread1.join()
