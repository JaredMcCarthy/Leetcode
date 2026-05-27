---
title: "3516. Find Closest Person"
---

<div class="problem-header">
  <div class="problem-number">3516</div>
  <div>
    <div><strong>Find Closest Person</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Math</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def findClosest(self, x, y, z):
        persona1 = abs(x - z)
        persona2 = abs(y - z)
        persona3 = persona1 - persona2

        if persona1 < persona2:
            return 1
        elif persona2 < persona1:
            return 2
        else:
            return 0

sol = Solution()
print(sol.findClosest(2, 7, 4))
print(sol.findClosest(2, 5, 6))
print(sol.findClosest(1, 5, 3))
```

<div class="navigation">
  <a class="prev" href="../smallest-number-with-all-set-bits/">Anterior</a>
  <a class="next" href="../minimum-operations-to-convert-all-elements-to-zero/">Siguiente</a>
</div>
