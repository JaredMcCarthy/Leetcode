---
title: "18. 4Sum"
---

<div class="problem-header">
  <div class="problem-number">18</div>
  <div>
    <div><strong>4Sum</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Array, Sorting, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result, quad = [], []

        def ksum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    ksum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            
            l,r = start, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    result.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        ksum(4, 0, target)
        return result

sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], target=0))
print(sol.fourSum([2,2,2,2,2], target=8))
```

<div class="navigation">
  <a class="prev" href="../3sum-closest/">Anterior</a>
  <a class="next" href="../valid-parentheses/">Siguiente</a>
</div>
