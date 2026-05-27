---
title: "1526. Minimum number of increments on subarrays to form a target array"
---

<div class="problem-header">
  <div class="problem-number">1526</div>
  <div>
    <div><strong>Minimum number of increments on subarrays to form a target array</strong> <span class="badge-hard">Hard</span></div>
    <div><strong>Tags:</strong> Array, Dynamic Programming, Greedy, Monotonic Stack, Stack</div>
  </div>
</div>

## Solución (Python)

```python
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
```

<div class="navigation">
  <a class="prev" href="../check-if-all-1s-are-at-least-length-k-places-away/">Anterior</a>
  <a class="next" href="../minimum-time-to-make-rope-colorful/">Siguiente</a>
</div>
