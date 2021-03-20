import threading
import time

def printtime(name):
    count=0
    #dly = time.time()
    for count in range(15_000_000):
        count+=1
    #print(name, "  " , time.time()-dly)


def printdly(name):
    count=0
    #dly = time.time()
    time.sleep(1)
    #print(name, " ", time.time()-dly)


if __name__ == "__main__":
    str = '''
calling loop function that utilizes the cpu.
Threading is not helpful in this case.
    '''
    print(str)

    print("calling printtime")

    dly=time.time()
    printtime("thread1")
    printtime("thread2")
    printtime("thread3")
    printtime("thread4")
    print("done in ", time.time()-dly)

    print("calling printtime threads")

    dly=time.time()
    t1 = threading.Thread(target=printtime,args=('thread1',))
    t2 = threading.Thread(target=printtime,args=('thread2',))
    t3 = threading.Thread(target=printtime,args=('thread3',))
    t4 = threading.Thread(target=printtime,args=('thread4',))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("Threads done in ", time.time()-dly)

    str='''
Calling a method that uses time.sleep(1).
Threading will be helpful here as other threads can execute
in the mean time
    '''
    print(str)
    print("calling printdly")
    dly=time.time()
    printdly("thread1")
    printdly("thread2")
    printdly("thread3")
    printdly("thread4")
    print("DLY done in ", time.time()-dly)

    print("starting printdly threads")
    dly=time.time()
    t1 = threading.Thread(target=printdly,args=('thread1',))
    t2 = threading.Thread(target=printdly,args=('thread2',))
    t3 = threading.Thread(target=printdly,args=('thread3',))
    t4 = threading.Thread(target=printdly,args=('thread4',))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("DLY Threads done in ", time.time()-dly)




    
