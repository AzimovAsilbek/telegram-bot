import time
import threading
import multiprocessing
from turtledemo.penrose import start

#multitasking threading orqali jarayonlar navbat bilan bajaradi

# SLEEP = 5

# def multitask():
#     time.sleep(SLEEP)
    # print(f"{SLEEP} shunch sekun kutildi")


# def multitask2():
#     time.sleep(SLEEP)
    # print(f"{SLEEP} shuncha sekund kutildi")

# thread1 = threading.Thread(target=multitask)
# thread2 = threading.Thread(target=multitask2)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()

#Parallelism Multiprocessing orqali jarayoni parallel bajaradi

# SLEEP2 = 5

# def multiprocessing_task1():
#     time.sleep(SLEEP2)
    # print(f"{SLEEP2} shuncha sekund ketdi")

#
# def multiprocessing_task2():
#     time.sleep(SLEEP2)
    # print(f"{SLEEP2} shuncha sekund ketdi")

# processing1 = multiprocessing.Process(target=multiprocessing_task1())
# processing2 = multiprocessing.Process(target=multiprocessing_task2())
#
# processing1.start()
# processing2.start()
#
# processing1.join()
# processing2.join()

#Multitasking va Multiprocessing ni farqi

SLEEP3 = 10

def func(name):
    time.sleep(SLEEP3)
    # print(f"{SLEEP3} sekund kutildi: {name}")


def multitasking():
    start1 = time.time()

    threads1 = threading.Thread(target=func, args=("Thread1",))
    threads2 = threading.Thread(target=func, args=("Thread2",))


    threads1.start()
    threads2.start()

    threads1.join()
    threads2.join()

    end = time.time()

    # print(f"Multitasking: {end - start1:.2f} secund")   #10.00 secund

def multiprocessing_func():
    start2 = time.time()

    process1 = multiprocessing.Process(target=func, args=("Process1",))
    process2 = multiprocessing.Process(target=func, args=("Process2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end2 = time.time()

    # print(f"Multiprocessing: {end2 - start2:.2f} secund")  #10.13 secund

if __name__ == "__main__":
    multitasking()
    multiprocessing_func()

