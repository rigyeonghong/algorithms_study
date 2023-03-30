import sys
first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
third = sys.stdin.readline().strip()

def diff(a, b):
    matrix = [[0] * (len(a)+1) for _ in range(len(b)+1)]   
    result = ''
    max_val = 0
    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            if b[i-1] == a[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                if matrix[i][j] > max_val:
                    result += b[i-1]
                    max_val = matrix[i][j]
            else: 
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j]) 
    return result

result_ab = diff(second, first)
ans = diff(result_ab, third)
print(len(ans))

'''
abbbccc
bbbaddd
cccddda

1
'''