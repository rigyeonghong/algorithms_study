class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        square = num**(1/2)
        if int(square) == square: return True
        else: return False

solution = Solution()
print(solution.isPerfectSquare(16))