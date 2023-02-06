import sys
n = int(sys.stdin.readline())
A, B, C= 300, 60, 10
answer = []

if n >= A:
    answer.append(n // A)
    n = n%A
else: answer.append(0)

if n >= B:
    answer.append(n // B)
    n = n%B
else: answer.append(0)
    
if n >= C:
    answer.append(n // C)
    n = n%C
else: answer.append(0)

if n == 0: print(*answer)
else: print(-1)