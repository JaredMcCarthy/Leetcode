---
title: "1317. Convert Integer to the Sum of Two No-Zero Integers"
---

<div class="problem-header">
  <div class="problem-number">1317</div>
  <div>
    <div><strong>Convert Integer to the Sum of Two No-Zero Integers</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Math</div>
  </div>
</div>

## Solución (Python)

```python
class Solution(object):
    def getNoZeroIntegers(self, n):
        a = 1
        b = n - a

        while '0' in str(a) or '0' in str(b):
            a += 1
            b = n - a
            if a > n:
                return None, None
        return [a, b]

sol = Solution()
print(sol.getNoZeroIntegers(2))
print(sol.getNoZeroIntegers(11))
```

<div class="navigation">
  <a class="prev" href="../valid-triamgle-number/">Anterior</a>
  <a class="next" href="../check-if-all-1s-are-at-least-length-k-places-away/">Siguiente</a>
</div>
