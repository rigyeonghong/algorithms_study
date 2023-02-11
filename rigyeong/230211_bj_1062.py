import sys
n, k = map(int, sys.stdin.readline().split())
alphabet = [0] * 26
ans = 0
words = [set(sys.stdin.readline().strip()[4:-4]) for _ in range(n)]

def get_readable():
    result = 0
    for word in words:
        flag = True
        for w in word:
            if not alphabet[ord(w) - ord('a')]:
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
        if not alphabet[i]:
            alphabet[i] = 1
            dfs(i, depth+1)
            alphabet[i] = 0

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    learned = {"a","n","t","i","c"}
    for l in learned:
        alphabet[ord(l)- ord('a')] = 1
    dfs(0,5)
    print(ans)

'''
3 6
antahtica
antacartica
antarctica

anta h tica
anta car tica
anta rc tica
'''