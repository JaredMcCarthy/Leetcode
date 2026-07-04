class Solution(object):
    def getNoZeroIntegers(self, n):
        a = 1
        b = n - a

        while '0' in str(a) or '0' in str(b):
            a += 1
            b = n - a
            if a > n:
                return None, None
        return [a, b]

sol = Solution()
print(sol.getNoZeroIntegers(2))
print(sol.getNoZeroIntegers(11))