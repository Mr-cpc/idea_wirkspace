from basic.bupt_2017_10_30.deco import time_statistic


def dfs(s:str, encoder_set:dict):
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return 1 if s != "0" else 0
    else:
        if s[:2] not in encoder_set:
            if s[0] == "0":
                return 0
            else:
                return dfs(s[1:],encoder_set)
        else:
            return dfs(s[2:],encoder_set) + (dfs(s[1:],encoder_set) if s[0] != "0" else 0)

@time_statistic
def decways(s:str) -> int:
    encoder_set = {str(num + 1) : chr(num+ord('A')) for num in range(26)}
    return dfs(s,encoder_set)


print(decways("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))