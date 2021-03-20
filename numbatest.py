from numba import jit
import time

@jit()
def do_something():
    print("started")
    
    for i in range (400_000_000):
        pass


def do_something2():
    print("started")
    
    for i in range (400_000_000):
        pass


t = time.time()
do_something()
print(f"done in jit {time.time() - t}")

t = time.time()
do_something2()
print(f"done in python {time.time() - t}")
