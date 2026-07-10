
class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        usuarios_problematicos = set()

        for a, b in friendships:
            if set(languages[a -1]).isdisjoint(set(languages[b-1])):
                usuarios_problematicos.add(a)
                usuarios_problematicos.add(b)

        respuesta = float('inf')

        for idioma_b in range(1, n + 1):
            contador = 0

            for u in usuarios_problematicos:
                if idioma_b not in languages[u - 1]:
                    contador += 1

            respuesta = min(respuesta, contador)

        return respuesta

sol = Solution()
print(sol.minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]))
print(sol.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]))
