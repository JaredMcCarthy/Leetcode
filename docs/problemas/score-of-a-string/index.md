---
title: "3110. Score of a String"
---

<div class="problem-header">
  <div class="problem-number">3110</div>
  <div>
    <div><strong>Score of a String</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> String</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def scoreOfString(self, s):
        total_inicial = 0

        for i in range(len(s) - 1):
            num1 = ord(s[i])
            num2 = ord(s[i + 1])
            diferencia = abs(num1 - num2)
            total_inicial = total_inicial + diferencia

        return total_inicial

sol = Solution()
print(sol.scoreOfString("hello"))
print(sol.scoreOfString("zaz"))
```

<div class="navigation">
  <a class="prev" href="../minimum-operations-to-make-the-integer-zero/">Anterior</a>
  <a class="next" href="../find-x-sum-of-all-k-long-subarrays-ii/">Siguiente</a>
</div>
