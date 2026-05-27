---
title: "31. Next Permutation"
---

<div class="problem-header">
  <div class="problem-number">31</div>
  <div>
    <div><strong>Next Permutation</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Array, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python


class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        right_nega = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_nega = i
                break
        
        if right_nega != -1:
            left_nega = -1
            for j in range(n - 1, right_nega, -1):
                if nums[j] > nums[right_nega]:
                    left_nega = j
                    break

            nums[right_nega], nums[left_nega] = nums[left_nega], nums[right_nega]

        left = right_nega + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

sol = Solution()
print(sol.nextPermutation([1,2,3]))
print(sol.nextPermutation([3,2,1]))
print(sol.nextPermutation([1,1,5]))
```

<div class="navigation">
  <a class="prev" href="../find-the-index-of-the-first-occurrence-in-a-string/">Anterior</a>
  <a class="next" href="../search-in-rotated-sorted-array/">Siguiente</a>
</div>
