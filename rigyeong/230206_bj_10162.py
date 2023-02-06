import sys
n = int(sys.stdin.readline())
if n % 10 != 0:
    print(-1)
else: 
    print(n//300, (n%300)//60, ((n%300)%60)//10)