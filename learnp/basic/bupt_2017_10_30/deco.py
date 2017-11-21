import time


def time_statistic(fun):
    def wrapper(*args,**kwargs):
        st = time.time()
        res = fun(*args,**kwargs)
        en = time.time()
        print("spend time {}ms".format((en -st)))
        return res
    return wrapper

@time_statistic
def myfun():
    time.sleep(1)
    print("a")

myfun()