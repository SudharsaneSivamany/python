from threading import *
from time import sleep

class proc1(Thread):
    def run(self):
        for i in range(20):
            print("process-1")
            sleep(1)

class proc2(Thread):
    def run(self):
        for i in range(15):
            print("process-2")
            sleep(1)

p1 = proc1()
p2 = proc2()

p1.start()
sleep(0.2)
p2.start()

p1.join()
p2.join()

print("done")
