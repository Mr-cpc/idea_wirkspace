'''
four led represents the hours
six leds represents the minutes
n represents the numbers of the leds that are on 
'''


def _com(sou:list,cur:list,k:int,res:list):
    if k == 0:
        res.append(cur)
    sou_copy = sou[:]
    for num in sou:
        cur.append(num)
        sou_copy.remove(num)
        _com(sou_copy,cur[:],k-1,res)
        cur.remove(num)


def com(n:int,k:int) ->list:
    res = []
    _com(list(range(n)),[],k,res)
    return res


def get_bin_time_str(h:list,time:list):
    res = []
    for on in h:
        for bit in on :
            time[bit] = 1
        res.append("".join(str(i) for i in time))
        for i in range(len(time)):
            time[i] = 0
    return res


def biwa(num:int)->list:
    h = [0] * 4
    m = [0] * 6
    res = []
    for i in range(0,num+1):
        num_h = get_bin_time_str(com(4,i),h)
        num_m = get_bin_time_str(com(6,num-i),m)
        for hour in num_h:
            for mte in num_m:
                hour_dec,mte_dec = int(hour,2),int(mte,2)
                if hour_dec < 12 and mte_dec < 60:
                    res.append("{}:{}".format(hour_dec,str(mte_dec).zfill(2)) )
    return res

print(biwa(0))