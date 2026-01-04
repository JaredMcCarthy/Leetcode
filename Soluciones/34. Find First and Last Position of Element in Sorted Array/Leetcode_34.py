

class Solution:
    def searchRange(self, nums, target):
        n = sorted(nums)

        first = -1
        last = -1

        for i in range(len(n)):
            if target != nums[i]:
                continue

            if first == -1:
                first = i

            last = i

        return [first, last]


# Tests
nums1 = [5,7,7,8,8,10]      # 3 y 4
target1 = 8

nums2 = [5,7,7,8,8,10]
target2 = 6

nums3 = []
target3 = 0


sol = Solution()
print(sol.searchRange(nums1, target1))
print(sol.searchRange(nums2, target2))
print(sol.searchRange(nums3, target3))


# Esta es una solucion que se supone que funcionaba pero ya olvide como.

        # n = sorted(nums)

        # resultado = []

        # left = 0
        # right = len(n) - 1

        # for i in range(len(nums)):
        #     if nums[left] == target:
        #         return nums[i]
        #         resultado.append(nums[i])
        #     else:
        #         left += 1

        #     for j in range(len(nums) - 1 ,- 1):
        #         if nums[right] == target:
        #             return nums[j]
        #             resultado.append(nums[j])
        #         else:
        #             right -= 1

        # for i in range(len(nums)):
        #     if nums[left] and nums[right] != target:
        #         return [-1, -1]