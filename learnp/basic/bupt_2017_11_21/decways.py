def dfs(s:str, encoder_set:dict):
    if len(s) in (0 ,1):
        return 1
    else:
        if int(s[:2]) not in encoder_set:
            return dfs(s[1:],encoder_set)
        else:
            return dfs(s[2:],encoder_set) + dfs(s[1:],encoder_set)


def decways(s:str) -> int:
    encoder_set = {num + 1 : chr(num+ord('A')) for num in range(26)}
    return dfs(s,encoder_set)
