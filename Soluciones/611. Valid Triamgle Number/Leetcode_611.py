
class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        contador = 0

        for k in range(len(nums) -1, -1, -1):
            lado_largo = nums[k]

            i = 0
            j = k - 1

            while i < j:
                lado_a = nums[i]
                lado_b = nums[j]

                if lado_a + lado_b > lado_largo:
                    contador += (j - i)
                    j -= 1
                else:
                    i += 1

        return contador

sol = Solution()
print(sol.triangleNumber([2,2,3,4]))
print(sol.triangleNumber([4,2,3,4]))