
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

sol = Solution()
print(sol.isPowerOfTwo(1))
print(sol.isPowerOfTwo(16))
print(sol.isPowerOfTwo(3))