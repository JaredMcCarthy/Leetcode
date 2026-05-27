class Solution(object):
    def minNumberOperations(self, target):
        prev = 0
        steps = 0
        
        for num in target:
            diff = num - prev
            if diff > 0:
                steps += diff
            prev = num
        
        return steps

sol = Solution()
print(sol.minNumberOperations([1,2,3,2,1]))