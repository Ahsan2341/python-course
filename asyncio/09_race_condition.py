import threading
chai_stock=0

def restock():
    global chai_stock
    for i in range(100000):
        chai_stock+=1


threads=[threading.Thread(target=restock) for i in range(2)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
print("chai stock", chai_stock)