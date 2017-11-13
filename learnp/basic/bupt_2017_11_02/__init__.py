import heapq

x = [float("inf")] * 4
heapq.heapify(x)
for i in range(4):
    print(i < x[0])
    if i < x[0]:
        heapq.heappushpop(x,i)
print(x)