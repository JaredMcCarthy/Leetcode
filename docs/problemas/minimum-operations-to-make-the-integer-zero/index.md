---
title: "2749. Minimum Operations to Make the Integer Zero"
---

<div class="problem-header">
  <div class="problem-number">2749</div>
  <div>
    <div><strong>Minimum Operations to Make the Integer Zero</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Bit Manipulation, Brainteaser, Enumeration</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def makeTheIntegerZero(self,num1,num2):
        x = num1
        y = num2
        k = 1

        while True:
            x = x - y
            if x < k:
                return -1
            
            if bin(x).count('1') <= k:
                return k

            k = k + 1

sol = Solution()
print(sol.makeTheIntegerZero(3, -2))
print(sol.makeTheIntegerZero(5, 7))
```

<div class="navigation">
  <a class="prev" href="../determine-if-two-events-have-conflict/">Anterior</a>
  <a class="next" href="../score-of-a-string/">Siguiente</a>
</div>
