
class Solution(object):
    def minCost(self, colors, neededTime):
        prev = 0
        minTime = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[prev]:
                if neededTime[i] > neededTime[prev]:
                    minTime += neededTime[prev]
                    prev = i
                else:
                    minTime += neededTime[i]
            
            else:
                prev = i
        
        return minTime

sol = Solution()
print(sol.minCost("abaac", [1,2,3,4,5]))
print(sol.minCost("abc", [1,2,3]))
print(sol.minCost("aabaa", [1,2,3,4,1]))