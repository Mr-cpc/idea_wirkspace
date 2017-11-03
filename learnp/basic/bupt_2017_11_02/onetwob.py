'''
one bit 0
two bit 10/11
'''

'''
determine the bits is valid of the rules
'''
def check(bits:list):
    if len(bits) == 0:
        return True
    elif len(bits) == 1:
        return bits[0] == 0
    elif len(bits) == 2:
        return bits == [0,0] or (bits[0] == 1 and bits[1] in (0,1))
    else:
        if bits[0] == 0:
            return check(bits[1:])
        else:
            return check(bits[2:])


def isone(bits:list):
    if len(bits) < 2:
        return bits[0] == 0
    else:
        if bits[-2] == 1:
            return not check(bits[:-2])
        else:
            return check(bits[:-1])

bits = [0,0,0]

print(isone(bits))