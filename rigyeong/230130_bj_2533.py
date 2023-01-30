import sys
sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
dp = [[0,0] for i in range(n+1)]
visited = [0 for i in range(n+1)]

def dfs(start):
    visited[start] = 1
    if len(graph[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0 
    else:
        for i in graph[start]: 
            if visited[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0], dp[i][1]) # 친구가 얼리어탑터여도 아니어도 되서 둘 중 작은 거 
                dp[start][0] += dp[i][1] # 친구들 무조건 얼리어답터
        dp[start][1] += 1 

dfs(1)
print(min(dp[1][0], dp[1][1]))