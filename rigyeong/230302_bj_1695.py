# 틀린 풀이) 반례2
# import sys
# n = int(sys.stdin.readline())
# input = list(map(int, sys.stdin.readline().split()))

# start = 0
# end = n-1
# cnt1 = 0
# while start < end:
#     if input[start] != input[end]: # 맨 앞이랑 맨 뒤랑 다르면
#         cnt1 += 1
#         start += 1
#     else:
#         start += 1
#         end -= 1

# cnt2 = 0
# start = 0

# while start < end:
#     if input[start] != input[end]: # 맨 앞이랑 맨 뒤랑 다르면
#         cnt2 += 1
#         end -= 1
#     else:
#         start += 1
#         end -= 1

# print(min(cnt1,cnt2))

# ref 정답
n = int(input())
seq = list(map(int, input().split()))

dp = [[0]*(n+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if seq[-i]==seq[j-1] : dp[i][j] = dp[i-1][j-1]+1
        else : dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(n-dp[n][n])
'''
반례1
3
1 1 2  

1

반례2
10
1 5 9 3 2 3 6 8 9

5
'''