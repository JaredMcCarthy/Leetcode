---
title: "27. Remove Element"
---

<div class="problem-header">
  <div class="problem-number">27</div>
  <div>
    <div><strong>Remove Element</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python
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
```

<div class="navigation">
  <a class="prev" href="../remove-duplicates-from-sorted-array/">Anterior</a>
  <a class="next" href="../find-the-index-of-the-first-occurrence-in-a-string/">Siguiente</a>
</div>
