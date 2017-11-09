def kbr(words:list) ->list:
    row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    sets = [row1,row2,row3]
    d = {s:0 for s in sets}
    ans = []
    for word in words:
        for ch in word:
            for s in sets:
                if ch.lower() in s:
                    d[s] += 1
        if len(word) in d.values():
            ans.append(word)
        for key in d:
            d[key] = 0
    return ans
