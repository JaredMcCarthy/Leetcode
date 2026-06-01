
class Solution(object):
    def permute(self, nums):
        results = []

        def backtrack(start, end):
            if start == end:
                results.append(nums[:])
                return
            
            for number in range(start, end):
                nums[number], nums[start] = nums[start], nums[number]
                backtrack(start + 1, end)
                nums[start], nums[number] = nums[number], nums[start]

        backtrack(0, len(nums))
        return results

sol = Solution()
print(sol.permute([1,2,3]))
print(sol.permute([0,1]))
print(sol.permute([1]))