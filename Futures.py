import concurrent.futures
import time

def do_something(name):
    for _ in range(100_000_000):
        pass
    return "done ", name

def done_something(var):
    print ("done something result = ", var.result())

if __name__ == "__main__":
    dly = time.perf_counter()
    print (dly)
    with concurrent.futures.ProcessPoolExecutor() as exec:
        f1 = [exec.submit(do_something, i) for i in range(3)]

    for f in f1:
        f.add_done_callback(done_something)


    print ("done with futures")    
    dly = time.perf_counter()
    print (dly)
