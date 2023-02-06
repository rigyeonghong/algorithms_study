from collections import deque
def solution(queue1, queue2):
    cnt = 0
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    
    while True:
        if sum1 < sum2:
            q = q2.popleft()
            q1.append(q)
            sum1 += q
            sum2 -= q
            cnt += 1
        elif sum1 > sum2:
            q = q1.popleft()
            q2.append(q)
            sum2 += q
            sum1 -= q
            cnt += 1
        else:
            break
        if cnt == (len(q1)) * 2: # 두 큐의 길이가 같기에 2배면 q1,q2가 위치만 바꾼 원래 큐라 생각.
            cnt = -1
            break
    
    return cnt