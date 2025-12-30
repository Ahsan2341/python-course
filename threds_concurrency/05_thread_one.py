import threading
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk boiled...")

def toast_bun():
    print(f"Toasting bun...")
    time.sleep(3)
    print(f"Done with bun toasting..")


start=time.time()
boil_thread=threading.Thread(target=boil_milk)
toast_thread=threading.Thread(target=toast_bun)

boil_thread.start()
toast_thread.start()

boil_thread.join()
toast_thread.join()

end = time.time()

print(f"Time taken {end-start :.2f} seconds")