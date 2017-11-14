def left_can_place(i, flowerbed):
    return i - 1 < 0 or flowerbed[i-1] == 0


def rigth_can_place(i, flowerbed):
    return i + 1 >= len(flowerbed) or flowerbed[i+1] == 0


def flower(flowerbed:list,n:int) ->bool:
    for i in range(len(flowerbed)):
        if n == 0:
            return True
        elif flowerbed[i] == 1:
            continue
        else:
            if left_can_place(i,flowerbed) and rigth_can_place(i,flowerbed):
                n -= 1
                flowerbed[i] = 1
            else:
                continue

    return n == 0

print(flower([1,0,0,0,1,0,0],2))