---
title: "231. Power of Two"
---

<div class="problem-header">
  <div class="problem-number">231</div>
  <div>
    <div><strong>Power of Two</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Bit Manipulation, Math, Recursion</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

sol = Solution()
print(sol.isPowerOfTwo(1))
print(sol.isPowerOfTwo(16))
print(sol.isPowerOfTwo(3))
```

<div class="navigation">
  <a class="prev" href="../palindrome-patitioning/">Anterior</a>
  <a class="next" href="../power-of-three/">Siguiente</a>
</div>
