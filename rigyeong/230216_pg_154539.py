# ref
from collections import deque
def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack=deque()
    
    for i,num in enumerate(numbers):
        while len(stack) and stack[-1][0]<num:
            answer[stack[-1][1]]=num
            stack.pop()
        
        stack.append((num,i))
    
    return answer


# 시간 초과
def solution(numbers):
    answer = []
    for idx, num in enumerate(numbers):
        flag = False
        while idx != len(numbers)-1 or numbers[idx] <= num:
            idx += 1
            if idx == len(numbers):
                break
            if numbers[idx] > num:
                answer.append(numbers[idx])
                flag = True
                break
        if flag == False:
            answer.append(-1)
            
    return answer