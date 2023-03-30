import sys
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()

a = len(A) 
b = len(B) 
c = len(C) 

matrix = [[[0]*(c+1) for _ in range(b+1)] for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            if A[i-1] == B[j-1] == C[k-1]:
                matrix[i][j][k] = matrix[i-1][j-1][k-1] +1
            else:
                matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j-1][k], matrix[i][j][k-1])

ans = 0
for i in range(a+1):
    for j in range(b+1):
        ans = max(ans, max(matrix[i][j]))
print(ans)