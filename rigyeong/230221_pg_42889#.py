#24분
from heapq import heappush, heappop
def solution(N, stages):
    result = []
    stage = [0] * (N+2)
    
    for s in stages:
        stage[s] +=1

    players = len(stages)
    for idx, s in enumerate(stage):
        if s == 0: continue
        stage[idx] = s / players
        players -= s

    heap = []
    for i in range(1,len(stage)-1):
        heappush(heap, (-stage[i],i))
    while heap:
        result.append(heappop(heap)[1])
        
    return result