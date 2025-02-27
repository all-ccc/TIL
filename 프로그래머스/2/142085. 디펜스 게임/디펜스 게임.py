from heapq import heappush, heappop

def solution(n, k, enemy):
    maxWin = 0
    sumEnemy = 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            if k == 0: break
            sumEnemy += heappop(heap)
            k -= 1
        maxWin += 1
    
    return maxWin