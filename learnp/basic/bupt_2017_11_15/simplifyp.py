import re
def simplifyP(path:str) -> str:
    path = re.sub("//*","/",path)
    dirs = path.split("/")
    stk = []
    for i in dirs:
        if i in ("","."):
            continue
        elif i == "..":
            if len(stk):
                stk.pop()
            else:
                continue
        else:
            stk.append(i)

    return "/{}".format("/".join(stk))






x = simplifyP("/../a///b/c//f/../e")
print(x)