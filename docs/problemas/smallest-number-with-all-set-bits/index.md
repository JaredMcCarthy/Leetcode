---
title: "3370. Smallest number with All Set Bits"
---

<div class="problem-header">
  <div class="problem-number">3370</div>
  <div>
    <div><strong>Smallest number with All Set Bits</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Bit Manipulation, Math</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def smallestNumber(self, n):
        return (1 << n.bit_length()) - 1

sol = Solution()
print(sol.smallestNumber(5))
```

<div class="navigation">
  <a class="prev" href="../find-x-sum-of-all-k-long-subarrays-ii/">Anterior</a>
  <a class="next" href="../find-closest-person/">Siguiente</a>
</div>
