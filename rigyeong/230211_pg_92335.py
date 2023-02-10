import math
def change(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k) # 첫번째 인자를 두번째 인자로 나눈 몫과 나머지 반환
        rev_base += str(mod)
    return rev_base[::-1] # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

def isPrime(n):
    for i in range (2, int(math.sqrt(n) + 1)):	# 2부터 n의 제곱근까지의 숫자
    	if n % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
        	return False
    return True	
    # for i in range(2, n): # 속도 느림
    #     if n % i == 0:
    #         return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    # return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴

def solution(n, k):
    num = change(n, k)
    num = str(num).split('0')
    
    cnt = 0
    for n in num:
        if n == '' or n == '1':
            continue
        n = int(n)
        if isPrime(n):
            cnt +=1
    
    return cnt