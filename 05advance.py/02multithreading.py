#multithreading -> a way of achieving multitasking

'''
Components of a process
-> executable program
-> associated data needed in the program(variables)
-> execution context of the program(state)

thread -> sequence of instructions within a program that can be executed independently of other code
'''


import threading
import os

import time

# def cube(n):
#     print(f"cube of {n} is {n**3}")

# def square(n):
#     print(f"square of {n} is {n**2}")


# t1 = threading.Thread(target=cube, args=(10,))
# t2 = threading.Thread(target=square, args=(10,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("end")

# def task1():
#     print(f"Task 1 is assigned to thread : {threading.current_thread().name}")
#     print(f"ID of process running task 1: {os.getpid()}")

# def task2():
#     print(f"Task 2 is assigned to thread : {threading.current_thread().name}")
#     print(f"ID of process running task 2: {os.getpid()}")

# if __name__ == "__main__":
#     print(f"Main thread : {threading.current_thread().name}")
#     print(f"ID of process running main program: {os.getpid()}")

#     t1 = threading.Thread(target=task1, name="t1")
#     t2 = threading.Thread(target=task2, name="t2")

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()





# def print_numbers():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# def print_letters():
#     for letter in 'ABCDE':
#         print(letter)
#         time.sleep(1)

# if __name__ == "__main__":
#     # Create threads
#     thread1 = threading.Thread(target=print_numbers)
#     thread2 = threading.Thread(target=print_letters)

#     # Start threads
#     thread1.start()
#     thread2.start()

#     # Wait for threads to finish
#     thread1.join()
#     thread2.join()

#     print("Threads finished.")



import concurrent.futures
 
def worker():
    print("Worker thread running")
 
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
 
pool.submit(worker)
pool.submit(worker)
 
pool.shutdown(wait=True)
 
print("Main thread continuing to run")