#11653 소인수분해

import sys
from math import sqrt

readl = sys.stdin.readline


def prime(prime: int):
    root = int(sqrt(prime))
    div = 2
    while div <= root:
        if prime % div == 0:
            return False
        div += 1
    return True 
   
def soinsu(number: int):
    tmp = int(sqrt(number))
    div = 2
    while div <= tmp and (number > 1):
        if prime(div):
            while number % div == 0:
                print(div)
                number //= div
        div += 1
    if number > 1:
        print(int(tmp))
        
if __name__ == "__main__":
    number = readl()
    soinsu(int(number))

