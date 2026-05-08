---
title: "26. Remove Duplicates from Sorted Array"
---

<div class="problem-header">
  <div class="problem-number">26</div>
  <div>
    <div><strong>Remove Duplicates from Sorted Array</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python

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
```

<div class="navigation">
  <a class="prev" href="../merge-two-sorted-lists/">Anterior</a>
  <a class="next" href="../remove-element/">Siguiente</a>
</div>
