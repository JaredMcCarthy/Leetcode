
class Solution:
	def minOperations(self, nums):
		contador = 0

		while any(x != 0 for x in nums):
			grupos = self.separar_no_ceros(nums)

			for grupo in grupos:
				minimo_grupo = min(nums[idx] for idx in grupo)

				for posicion_original in grupo:
					nums[posicion_original] = nums[posicion_original] - minimo_grupo
				contador = contador + 1

		return contador

	def separar_no_ceros(self, nums):
		grupos = []
		grupo_actual = []

		for indice in range(len(nums)):
			if nums[indice] != 0:
				grupo_actual.append(indice)
			else:
				if grupo_actual:
					grupos.append(grupo_actual)
					grupo_actual = []

		if grupo_actual:
			grupos.append(grupo_actual)

		return grupos

sol = Solution()
print(sol.minOperations([0, 2]))  # 1
print(sol.minOperations([3, 1, 2, 1]))  # 3
print(sol.minOperations([1, 2, 1, 2, 1, 2]))  # 4










