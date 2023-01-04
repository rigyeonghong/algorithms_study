import sys
input = sys.stdin.readline

N = int(input())

divisor = 2

while divisor <= N:
    if N % divisor == 0:
        print(divisor)
        N = N // divisor
    else:
        divisor += 1