---
title: "69. Sqrt(x)"
---

<div class="problem-header">
  <div class="problem-number">69</div>
  <div>
    <div><strong>Sqrt(x)</strong> <span class="badge-medium">Unknown</span></div>
    <div><strong>Tags:</strong> —</div>
  </div>
</div>

## Solución (Python)

```python
class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x

        resultado = 0
        inicio = 1
        fin = x

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if medio * medio == x:
                return medio
            elif medio * medio < x:
                resultado = medio
                inicio = medio + 1
            elif medio * medio > x:
                fin = medio - 1

        return resultado
                    
sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(8))
```

<div class="navigation">
  <a class="prev" href="../add-binary/">Anterior</a>
  <a class="next" href="../climbing-stairs/">Siguiente</a>
</div>
