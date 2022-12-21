import sys
n = int(sys.stdin.readline())
div = 2
while n!=1:
    if n % div==0: 
        print(div) 
        n = n//div
    else:
        div += 1