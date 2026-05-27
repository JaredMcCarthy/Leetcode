---
title: "46. Permutations"
---

<div class="problem-header">
  <div class="problem-number">46</div>
  <div>
    <div><strong>Permutations</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Array, Backtracking</div>
  </div>
</div>

## Solución (Python)

```python

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
```

<div class="navigation">
  <a class="prev" href="../combination-sum/">Anterior</a>
  <a class="next" href="../length-of-last-word/">Siguiente</a>
</div>
