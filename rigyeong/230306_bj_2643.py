import sys 
n = int(sys.stdin.readline())
rectangles = [(1000, 1000)]
for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    rectangles.append((max(w, h), min(w, h)))
rectangles.sort(reverse=True)
dp = [[0, rectangles[i][1]] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(i-1, -1, -1):
        if dp[j][1] >= dp[i][1] and dp[j][0] + 1 > dp[i][0]:
            dp[i][0] = dp[j][0] + 1
            ans = max(ans, dp[i][0])
print(ans)