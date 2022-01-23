import heapq
n, b = [int(i) for i in input().split()]
gifts = []
heapq.heapify(gifts)
for i in range(n): 
    s, e = [int(j) for j in input().split()]
    summ = s+e
    heapq.heappush(gifts, [summ, s, e])
    

gifts = [heapq.heappop(gifts) for i in range(n)]
    
print(gifts)

can_buy = 0

for i in range(n): 
    temp = 0
    bb = b
    for j in range(n):
        cost = gifts[i][0]
        if i==j: 
            cost-=(gifts[i][1]/2)
        print(cost)
