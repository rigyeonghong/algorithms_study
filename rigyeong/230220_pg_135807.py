from math import gcd
def solution(arrayA, arrayB):
    answer = 0
    gcdA, gcdB = arrayA[0], arrayB[0]
    for a, b in zip(arrayA[1:], arrayB[1:]):
        gcdA, gcdB = gcd(a, gcdA), gcd(b, gcdB)

# 아래 코드로 실행시 test case 중 3개가 runtime error
#     def gcd(array): 
#         gcd_res = 0
#         for i in range(len(array)-1):
#             if gcd_res == 1: return gcd_res
        
#             if i == 0:
#                 gcd_res = math.gcd(array[i], array[i+1])
#             elif i+1 <= len(array):
#                 gcd_res = math.gcd(gcd_res, array[i+1])
#         return gcd_res

    if gcdA != 1:
        for b in arrayB:
            if b % gcdA == 0:
                break
        else: answer = gcdA # for문이 마지막 요소까지 모두 반복했을 시 수행, break 만나면 수행 안됨

    if gcdB != 1:
        for a in arrayA:
            if a % gcdB == 0:
                break
        else: answer = max(answer, gcdB)

    return answer
