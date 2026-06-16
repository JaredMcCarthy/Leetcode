class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x

        resultado = 0
        inicio = 1
        fin = x

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if medio * medio == x:
                return medio
            elif medio * medio < x:
                resultado = medio
                inicio = medio + 1
            elif medio * medio > x:
                fin = medio - 1

        return resultado
                    
sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(8))