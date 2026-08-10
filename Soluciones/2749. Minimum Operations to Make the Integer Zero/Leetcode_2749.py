
class Solution(object):
    def makeTheIntegerZero(self,num1,num2):
        x = num1
        y = num2
        k = 1

        while True:
            x = x - y
            if x < k:
                return -1
            
            if bin(x).count('1') <= k:
                return k

            k = k + 1

sol = Solution()
print(sol.makeTheIntegerZero(3, -2))
print(sol.makeTheIntegerZero(5, 7))