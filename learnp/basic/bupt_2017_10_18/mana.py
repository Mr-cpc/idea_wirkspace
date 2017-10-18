def mana(s):
    asis = []
    for ch in s:
        asis.append('#')
        asis.append(ch)
    asis.append('#')
    p = [0] * len(asis)
    cent,mxRight = 0,0
    for i in range(len(asis)):
        if i < mxRight:
            p[i] = min(p[2 * cent - i],mxRight - i)
        else:
            p[i] = 1
        while i+p[i] < len(asis) and i-p[i] >= 0 and asis[i+p[i]] == asis[i - p[i]]:
            p[i] += 1
        if p[i] + i - 1 > mxRight:
            mxRight,cent = p[i] + i -1,i
    return ''.join([asis[i] for i in range(cent - p[cent]+1,cent + p[cent]) if asis[i] != '#'])

print(mana(""))