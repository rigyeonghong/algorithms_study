'''
n이 점점 커지도록 정리되어 있는가
그렇지 않다면 가장 가까운 정리된 수를 찾자
'''
import sys

def isTidy(n):
    return list(str(n)) == sorted(list(str(n)))

def check(n):
    if isTidy(n):
        return n
    length = len(str(n))
    for i in range(1, length):
        a, b = divmod(n, 10**i) # 몫과 나머지
        target = str(a-1)+'9'*len(str(b))
        if isTidy(target):
            return int(target)

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    print(f"Case #{i+1}:",check(n))