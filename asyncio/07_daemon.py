import threading
import time

def monitor_tea_temp():
    while True:
        print("Tea temperature: 98.6°F")
        time.sleep(2)


thread=threading.Thread(target=monitor_tea_temp, daemon=True)
thread.start()

print("Main program done")
