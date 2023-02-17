from collections import defaultdict
def solution(clothes):
    answer = 1
    counter = defaultdict(int)
    for cloth, cloth_type in clothes:
        counter[cloth_type] += 1
    for c in counter:
        answer *= counter[c] + 1 
    return answer -1