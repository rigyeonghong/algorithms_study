# 코딩력이 부족한듯. dp를 동시에 진행하는 아이디어는 떠올랐으나 구현하지 못함.
import sys
n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
dp = [[0] * n for _ in range(2)]

dp[0][0] = seq[0] # 1개는 반드시 선택해야 한다.

if n > 1:
    ans = min(seq)
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1]+seq[i], seq[i])
        dp[1][i] = max(dp[0][i-1], dp[1][i-1]+seq[i])
        ans = max(ans, dp[0][i], dp[1][i])
    print(ans)
else:
    print(dp[0][0])