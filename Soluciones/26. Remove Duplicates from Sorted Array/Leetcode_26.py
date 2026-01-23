
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        j = 1
        for i in range(1, len(nums)):
             if nums[i] != nums[i - 1]:
                 nums[j] = nums[i]
                 j += 1
        return j

sol = Solution()
print(sol.removeDuplicates([1,1,2]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))