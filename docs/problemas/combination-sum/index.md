---
title: "39. Combination Sum"
---

<div class="problem-header">
  <div class="problem-number">39</div>
  <div>
    <div><strong>Combination Sum</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Array, Backtracking</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def combinationSum(self, candidates, target):
        resultado = []

        def combi_encontradas(combinaciones_actuales, inicio, actual_total):
            if actual_total == target:
                resultado.append(combinaciones_actuales[:])
            if actual_total > target:
                return
            
            for i in range(inicio, len(candidates)):
                numero = candidates[i]
                combinaciones_actuales.append(numero)
                combi_encontradas(combinaciones_actuales, i, actual_total + numero)
                combinaciones_actuales.pop()
        
        combi_encontradas([], 0, 0)
        return resultado

sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2,3,5], 8))
print(sol.combinationSum([2], 1))
```

<div class="navigation">
  <a class="prev" href="../search-insert-position/">Anterior</a>
  <a class="next" href="../permutations/">Siguiente</a>
</div>
