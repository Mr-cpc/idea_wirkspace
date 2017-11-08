def stcom(chars:list)->(list,int):
    i = 1
    d = {}
    while i < len(chars):
        if chars[i] == chars[i-1]:
            count = 1
            tmp = i #here is very important,otherwise the line 11 will record the last same character not the first
            while i < len(chars) and chars[i] == chars[i-1]:
                count += 1
                i += 1
            d[tmp-1] = list(str(count)) #here need use tmp not i
        else:
            i += 1
    new_chars = []
    i = 0
    while i < len(chars):
        # print("{}:{}".format(i,chars[i]))
        if i not in d:
            new_chars.append(chars[i])
            i += 1
        else:
            new_chars.append(chars[i])
            new_chars.extend(d[i])
            i += int("".join(d[i]))

    return new_chars,len(new_chars)


print(stcom(list("aaabbccc")))