from basic.bupt_2017_10_18.ptkes import n_comb


def worbk(s:str,wordDict:list) -> bool:
    wordDict = set(wordDict)
    if len(s) == 1:
        return s in wordDict
    for i in range(1,len(s)):
        candis = n_comb(list(range(1,len(s))),i)
        for parti in candis:
            st = 0
            parti.append(len(s))
            for p in parti:
                if s[st:p] in wordDict:
                    st = p
                else:
                    break
            else:
                return True
    return False

print(worbk("helloworld",["hello","world"]))