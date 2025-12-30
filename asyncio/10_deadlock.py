import threading

lock_a=threading.Lock()
lock_b=threading.Lock()


def task_1():
    with lock_a:
        print(f"Task 1 acquired lock A")
        with lock_b:
            print(f"Task 1 acquired lock B")


def task_2():
    with lock_b:
        print(f"Task 2 acquired lock B")
        with lock_a:
            print(f"Task 2 acquired lock A")

thread1=threading.Thread(target=task_1)
thread2=threading.Thread(target=task_2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()