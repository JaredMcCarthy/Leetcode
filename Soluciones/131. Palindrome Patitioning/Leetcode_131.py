
class Solution(object):
    def partition(self, s):
        resultado = []

        def backtracking(inicio, camino_actual):
            if inicio == len(s):
                resultado.append(list(camino_actual))
                return

            for i in range(inicio, len(s)):
                subcadena = s[inicio : i + 1]

                if subcadena == subcadena[::-1]:
                    camino_actual.append(subcadena)
                    backtracking(i + 1, camino_actual)
                    camino_actual.pop()
            
        backtracking(0, [])
        return resultado

sol = Solution()
print(sol.partition("aab"))
print(sol.partition("a"))