import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total=0
    for i in range(10**8):
        total+=i
    
    print("Done")

start=time.time()

threads= [threading.Thread(target=cpu_heavy) for _ in range(2)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]

end = time.time()

print(f"Time taken is {end-start:.2f} seconds")