# 백준 소인수분해 11653
n = int(input())

while(n != 1):
    for i in range(2, n+1):
        if n == i:
            print(i)
            n = int(n/i)
            break
        if n%i == 0:
            print(i)
            n = int(n/i)
            break