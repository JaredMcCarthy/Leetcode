from collections import Counter
class Solution:
    def findXSum(self, nums, k, x):
        resultado = []

        for i in range(len(nums) - k + 1):
            subarray = nums[i:i + k]

            # contamos las frecuencias del subbarray
            contador = Counter(subarray)

            # ordenamos por frec DESC Frecuen, valor DESC usando lambda
            element_ordenados = sorted(contador.items(), key=lambda item: (-item[1], -item[0]))

            # primero los elementos x
            top_x = element_ordenados[:x]

            # calculamos frecuencia x suma en cada elemento en top_x
            suma_actual = 0
            for valor, freq in top_x:
                suma_actual += valor * freq

            resultado.append(suma_actual)

        return resultado


sol = Solution()
print(sol.findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2))



#Solucion pero no optimizada.

