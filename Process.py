import multiprocessing
import time
import os

def do_something():    
    print("thread ", __name__)
    for _ in range(80_000_000):
        pass

if __name__ == '__main__':
    print("from main ", __name__)
    print ("cpu count = ", os.cpu_count())

    PROC = 5
    print("calling do_something ", PROC, " times")
    dly = time.time()
    for _ in range(PROC):
        do_something()

    print("done in ", time.time() - dly)

    print("starting ", PROC, " processes for do_something")
    dly = time.time()
    p = [multiprocessing.Process(target=do_something) for _ in range(PROC)]

    for pr in p:
        pr.start()

    for pr in p:
        pr.join()


    print("done in ", time.time() - dly)


    input("press any key...")
