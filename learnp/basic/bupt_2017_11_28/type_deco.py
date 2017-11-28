def tp_deco(fun):
    def wrapper(*args,**kwargs):
        fun("type:{}".format(type(*args)))
        fun(*args,**kwargs)
    return wrapper

@tp_deco
def prt(a):
    print(a)
