
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums)- 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum  = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return current_sum
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], target=1))
print(sol.threeSumClosest([0,0,0], target=0))