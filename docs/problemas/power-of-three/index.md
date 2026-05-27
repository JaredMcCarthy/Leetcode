---
title: "326. Power of Three"
---

<div class="problem-header">
  <div class="problem-number">326</div>
  <div>
    <div><strong>Power of Three</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Math, Recursion</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0 or n == 0:
            return False
        
        while n % 3 == 0:
            n = n // 3

        if n == 1:
            return True
        else:
            return False

sol = Solution()
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(0))
print(sol.isPowerOfThree(-1))
```

<div class="navigation">
  <a class="prev" href="../power-of-two/">Anterior</a>
  <a class="next" href="../valid-triamgle-number/">Siguiente</a>
</div>
