---
title: "131. Palindrome Patitioning"
---

<div class="problem-header">
  <div class="problem-number">131</div>
  <div>
    <div><strong>Palindrome Patitioning</strong> <span class="badge-medium">Unknown</span></div>
    <div><strong>Tags:</strong> —</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def partition(self, s):
        resultado = []

        def backtracking(inicio, camino_actual):
            if inicio == len(s):
                resultado.append(list(camino_actual))
                return

            for i in range(inicio, len(s)):
                subcadena = s[inicio : i + 1]

                if subcadena == subcadena[::-1]:
                    camino_actual.append(subcadena)
                    backtracking(i + 1, camino_actual)
                    camino_actual.pop()
            
        backtracking(0, [])
        return resultado

sol = Solution()
print(sol.partition("aab"))
print(sol.partition("a"))
```

<div class="navigation">
  <a class="prev" href="../symmetric-tree/">Anterior</a>
  <a class="next" href="../power-of-two/">Siguiente</a>
</div>
