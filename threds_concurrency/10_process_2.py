from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total=0
    for i in range(10**8):
        total+=i
    
    print("Done")

if __name__=="__main__":
    start=time.time()

    processes= [Process(target=cpu_heavy) for _ in range(2)]
    [process.start() for process in processes]
    [process.join() for process in processes]

    end = time.time()

    print(f"Time taken is {end-start:.2f} seconds")