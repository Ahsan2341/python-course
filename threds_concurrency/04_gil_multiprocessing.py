from multiprocessing import Process
import time

def crunchNumber():
    print(f"Started the count process..")
    count=0
    for i in range(100_000_000):
        count+=1
    print(f"Ended the count process..")


if __name__ == "__main__":
    start=time.time()
    process1=Process(target=crunchNumber)
    process2=Process(target=crunchNumber)

    process1.start()
    process2.start()


    process1.join()
    process2.join()

    end=time.time()

    print(f"Total time with multiprocessing is {end-start:.2f} seconds")