import sys
n, m = map(int, sys.stdin.readline().split())
blueray = list(map(int, sys.stdin.readline().split()))

result = sum(blueray)
s = result//m 
e = 10000000000

while s <= e :
    mid = (s+e) // 2
    if mid < max(blueray):
        s = mid + 1
        continue

    blue_cnt, blue_len = 1, 0

    for i in range(len(blueray)):
        if blue_len + blueray[i] <= mid: # 작으면 계속 더해줌
            blue_len += blueray[i]
        
        else: # 커지면 현재 blueray[i]가 blue_len으로 들어감
            blue_len = blueray[i]
            blue_cnt += 1
    
    if blue_cnt <= m: # bl
        e = mid - 1
        result = min(result, mid)
    else: # 갯수가 m 보다 크면 mid값 키우기 
        s = mid + 1
print(result)
