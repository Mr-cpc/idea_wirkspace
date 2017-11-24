import re


def rewoins(s:str):
    return " ".join(re.split(r"\s+",s.strip())[::-1])


print(rewoins(" the  blue sky  "))