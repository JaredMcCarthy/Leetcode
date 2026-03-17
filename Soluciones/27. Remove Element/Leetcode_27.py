class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    
sol = Solution()
print(sol.removeElement([3,2,2,3], 3))
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))