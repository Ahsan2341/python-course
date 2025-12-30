from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing.")
    time.sleep(3)  # Simulate time taken to brew chai
    print(f"End of {name} brewing.")

if __name__ == "__main__":
    chai_makers=[ Process(target=brew_chai, args=(f"Chai Maker {i+1}",)) for i in range(5)]

    # start all process
    for process in chai_makers:
        process.start()
    # wait for all process to complete
    for process in chai_makers:
        process.join()
        
    print("All chai brewing completed.")