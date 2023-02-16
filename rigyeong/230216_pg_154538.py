from collections import defaultdict, deque
def solution(x, y, n):
    if x == y: return 0
    q = deque([[x,0]])
    duplication = defaultdict(lambda: 0)

    while q:
        x, cnt = q.popleft()
        cnt += 1
        
        if duplication[x] == 1: continue
        else: duplication[x] = 1
        
        if x + n < y:
            q.append([x+n, cnt])
        elif x + n == y:
            return cnt
        
        if x*2 < y:
            q.append([x*2, cnt])
        elif x*2 == y:
            return cnt
        
        if x*3 < y:
            q.append([x*3, cnt])
        elif x*3 == y:
            return cnt
        
    return -1
print(solution(10, 40, 5))
