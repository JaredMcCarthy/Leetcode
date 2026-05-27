---
title: "2094. Finding 3-Digit Even Numbers"
---

<div class="problem-header">
  <div class="problem-number">2094</div>
  <div>
    <div><strong>Finding 3-Digit Even Numbers</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array, Enumeration, Hash Table, Recursion, Sorting</div>
  </div>
</div>

## Solución (Python)

```python
from collections import Counter


class Solution(object):
    def findEvenNumbers(self, digits):
            result = []
            digit_count = Counter(digits)
            for d1 in digit_count:
                if d1 == 0:
                    continue
                rest1 = digit_count.copy()
                rest1[d1] -= 1

                for d2 in rest1:
                    if rest1[d2] == 0:
                        continue
                    rest2 = rest1.copy()
                    rest2[d2] -= 1
                
                    for d3 in rest2:
                        if rest2[d3] == 0:
                            continue
                        if d3 % 2 != 0:
                            continue
                        numero = d1*100 + d2*10 + d3
                        result.append(numero)

            return sorted(result)

sol = Solution()
print(sol.findEvenNumbers([2,1,3,0]))
print(sol.findEvenNumbers([2,2,8,8,2]))
print(sol.findEvenNumbers([3,7,5]))
```

<div class="navigation">
  <a class="prev" href="../minimum-number-of-people-to-teach/">Anterior</a>
  <a class="next" href="../number-of-laser-beams-in-a-bank/">Siguiente</a>
</div>
