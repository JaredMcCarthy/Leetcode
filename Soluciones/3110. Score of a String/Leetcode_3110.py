
class Solution(object):
    def scoreOfString(self, s):
        total_inicial = 0

        for i in range(len(s) - 1):
            num1 = ord(s[i])
            num2 = ord(s[i + 1])
            diferencia = abs(num1 - num2)
            total_inicial = total_inicial + diferencia

        return total_inicial

sol = Solution()
print(sol.scoreOfString("hello"))
print(sol.scoreOfString("zaz"))