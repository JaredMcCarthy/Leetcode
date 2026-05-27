---
title: "67. Add Binary"
---

<div class="problem-header">
  <div class="problem-number">67</div>
  <div>
    <div><strong>Add Binary</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Bit Manipulation, Math, Simulation, String</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        resultado = []

        while i >= 0 or j >= 0 or carry:
            carry += (0 if i < 0 else int(a[i])) + (0 if j < 0 else int(b[j]))
            carry, v = divmod(carry, 2)

            resultado.append(str(v))

            i, j = i - 1, j - 1

        return "".join(resultado[::-1]) 

sol = Solution()
print(sol.addBinary("11", "1"))
print(sol.addBinary("1010", "1011"))
```

<div class="navigation">
  <a class="prev" href="../plus-one/">Anterior</a>
  <a class="next" href="../sqrt-x/">Siguiente</a>
</div>
