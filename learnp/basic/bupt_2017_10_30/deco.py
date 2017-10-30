import time

def time_statistic(fun):
    def wrapper():
        st = time.time()
        fun()
        en = time.time()
        print("spend time {}ms".format((en -st)))
    return wrapper

@time_statistic
def myfun():
    time.sleep(1)
    print("a")

myfun()