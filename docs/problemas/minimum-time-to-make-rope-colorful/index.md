---
title: "1578. Minimum Time to make rope colorful"
---

<div class="problem-header">
  <div class="problem-number">1578</div>
  <div>
    <div><strong>Minimum Time to make rope colorful</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Array, Dynamic Programming, Greedy, String</div>
  </div>
</div>

## Solución (Python)

```python

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
```

<div class="navigation">
  <a class="prev" href="../minimum-number-of-increments-on-subarrays-to-form-a-target-array/">Anterior</a>
  <a class="next" href="../minimum-number-of-people-to-teach/">Siguiente</a>
</div>
