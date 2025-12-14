

class Solution:
    def searchRotate(self, nums, target):
    	n = len(nums)
    	lo = 0
    	ri = n - 1

    	while lo <= ri:
    		mid = (lo + ri) // 2

    		if nums[mid] == target:
    			return mid

    		if nums[mid] >= nums[lo]:
    			if target >= nums[lo] and target < nums[mid]:
    				ri = mid - 1

    			else:
    				lo = mid + 1
    		else:
    			if target > nums[mid] and target <= nums[ri]:
    				lo = mid + 1
    			else:
    				ri = mid - 1

    	return -1



nums1 = [4,5,6,7,0,1,2]      #4
target1 = 0

nums2 = [4,5,6,7,0,1,2] #0
target2 = 3

nums3 = [1]    #0
target3 = 0


sol = Solution()
print(sol.searchRotate(nums1, target1))
print(sol.searchRotate(nums2, target2))
print(sol.searchRotate(nums3, target3))
