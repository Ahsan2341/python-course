import threading
import time

def take_orders():
    for i in range(1, 5):
        print(f"Taking order for {i}")
        time.sleep(1) 



def brew_chai():
    for i in range(1, 5):
        print(f"Brewing chai for {i}")
        time.sleep(2)

# create threads

orderThread=threading.Thread(target=take_orders) 
chaiThread=threading.Thread(target=brew_chai) 
orderThread.start()
chaiThread.start()

# wait for threads to complete
orderThread.join()
chaiThread.join()
print("All orders taken and chai brewed.")