---
title: "35. Search Insert Position"
---

<div class="problem-header">
  <div class="problem-number">35</div>
  <div>
    <div><strong>Search Insert Position</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array, Binary Search</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l

sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5,6], 7))
```

<div class="navigation">
  <a class="prev" href="../find-first-and-last-position-of-element-in-sorted-array/">Anterior</a>
  <a class="next" href="../combination-sum/">Siguiente</a>
</div>
