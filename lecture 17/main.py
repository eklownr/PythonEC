
import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")


def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Letter: {letter}")


counter = 0

def increment_counter():
    global counter
    for _ in range(1000000):
        current_value = counter
        current_value += 1
        counter = current_value


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread3 = threading.Thread(target=increment_counter)
thread4 = threading.Thread(target=increment_counter)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print(counter)
