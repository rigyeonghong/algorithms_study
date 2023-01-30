# 백준 숫자의합 11720
n = int(input())
number = input()
sum = 0
for i in range(n):
    sum += int(number[i])
print(sum)