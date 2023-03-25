import sys
n,m = map(int, sys.stdin.readline().split())
blueray = list(map(int, sys.stdin.readline().split()))

ans = sum(blueray)
start = max(blueray)
end = ans 

while start <= end:
    mid = (start + end) // 2
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
