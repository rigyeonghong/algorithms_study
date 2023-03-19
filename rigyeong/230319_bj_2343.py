import sys
n,m = map(int, sys.stdin.readline().split())
blueray = list(map(int, sys.stdin.readline().split()))

ans = sum(blueray)
start = ans//m
end = 10000000

while start <= end:
    mid = (start + end) // 2
    if mid < max(blueray): # 이게 포인트!! 밑에서 걸러주거나 해야함
        start = mid + 1
        continue

    cnt, len_blue = 1, 0
    for i in range(len(blueray)):
        add = len_blue + blueray[i]

        if add > mid:
            cnt += 1
            len_blue = blueray[i]
        else:
            len_blue = add
        
    if cnt <= m:
        ans = min(ans, mid)
        end = mid -1
    else:
        start = mid+1

print(ans)
