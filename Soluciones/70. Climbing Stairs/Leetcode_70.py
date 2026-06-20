
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2

        valor1 = 1
        valor2 = 2

        for i in range(3, n + 1):
            if i >= 3:
                nuevo = valor1 + valor2
                valor1 = valor2
                valor2 = nuevo
        
        return valor2

sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))