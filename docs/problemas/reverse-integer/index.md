---
title: "7. Reverse Integer"
---

<div class="problem-header">
  <div class="problem-number">7</div>
  <div>
    <div><strong>Reverse Integer</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Math</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def reverse(self, x):
        if x < 0:
            signo = -1
        else:
            signo = 1
        
        x = abs(x)
        resultado = 0

        while x > 0:
            digito = x % 10
            resultado = (resultado * 10 + digito)
            x = x // 10
            
        resultado = resultado * signo

        if resultado < -2147483648 or resultado > 2147483647:
            return 0
        else:
            return resultado

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))
```

<div class="navigation">
  <a class="prev" href="../longest-palindromic-substring/">Anterior</a>
  <a class="next" href="../palindrome-number/">Siguiente</a>
</div>
