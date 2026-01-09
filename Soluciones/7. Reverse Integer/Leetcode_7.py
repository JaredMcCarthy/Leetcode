
class Solution(object):
    def reverse(self, x):
        if x < 0:
            signo = -1
        else:
            signo = 1
        
        x = abs(x)
        resultado = 0

        while x > 0:
            digito = x % 10
            resultado = (resultado * 10 + digito)
            x = x // 10
            
        resultado = resultado * signo

        if resultado < -2147483648 or resultado > 2147483647:
            return 0
        else:
            return resultado

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))

