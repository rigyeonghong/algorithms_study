import sys
input = sys.stdin.readline
n, k = map(int, input().split())
words = [set(input().rstrip()[4:-4]) for _ in range(n)]
alphabets = [False] * 26
ans = 0

def get_readable():
    result = 0
    for word in words:
        flag = True
        for c in word:
            if not alphabets[ord(c) - ord('a')]:
                flag = False
                break
        if flag:
            result += 1
    return result

def dfs(start, depth):
    global ans
    if depth == k:
        ans = max(ans, get_readable())
        return

    for i in range(start, 26):
        if not alphabets[i]:
            alphabets[i] = True
            dfs(i, depth + 1)
            alphabets[i] = False

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    for c in ('a', 'c', 'i', 'n', 't'):
        alphabets[ord(c) - ord('a')] = True
    dfs(0, 5)
    print(ans)