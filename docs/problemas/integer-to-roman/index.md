---
title: "12. Integer to Roman"
---

<div class="problem-header">
  <div class="problem-number">12</div>
  <div>
    <div><strong>Integer to Roman</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Hash Table, Math, String</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def intToRoman(self, num):
        numeros_romanos = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        resultado = []

        for valor, simbolo in numeros_romanos:
            while num >= valor:
                resultado.append(simbolo)
                num -= valor

        return "".join(resultado)

sol = Solution()
print(sol.intToRoman(121234))
```

<div class="navigation">
  <a class="prev" href="../container-with-most-water/">Anterior</a>
  <a class="next" href="../roman-to-integer/">Siguiente</a>
</div>
