import threading
import time

class MyThreads():
    def __init__(self,name) -> None:
        self.thread=threading.Thread(target=self.thread_function,name=name)
        self.status=True

    def run(self):
        self.start_time=time.time()
        self.thread.start()

    def pause(self):
        self.status=False

    def resume(self):
        self.start_time=time.time()
        self.status=True

    def thread_function(self):
        while True:
            if self.status:
                print(f"{threading.current_thread().name} is running at {time.time()-self.start_time}")
                time.sleep(5)


if __name__=="__main__":
    t1=MyThreads("Thread 1")
    t2=MyThreads("Thread 2")
    t3=MyThreads("Thread 3")

    #starting thread 1 and thread 3
    t1.run()
    t3.run()

    #after 20 seconds stopping thread 1 and starting thread 2
    time.sleep(20)
    print("stopping thread 1 and starting thread 2")
    t1.pause()
    t2.run()

    #after 18 seconds stopping thread 3 and starting thread 1
    time.sleep(18)
    print("stopping thread 3 and starting thread 1")
    t3.pause()
    t1.resume()
    


    
    
    



