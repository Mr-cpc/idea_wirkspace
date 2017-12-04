import time


def time_statistic(fun):
    def wrapper(*args,**kwargs):
        st = time.time()
        res = fun(*args,**kwargs)
        en = time.time()
        print("{}() function spend time: {}s".format(fun.__name__,(en -st)))
        return res
    return wrapper

@time_statistic
def myfun(a):
    time.sleep(1)
    print("a")
