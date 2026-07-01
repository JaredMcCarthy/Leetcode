
class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0 or n == 0:
            return False
        
        while n % 3 == 0:
            n = n // 3

        if n == 1:
            return True
        else:
            return False

sol = Solution()
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(0))
print(sol.isPowerOfThree(-1))