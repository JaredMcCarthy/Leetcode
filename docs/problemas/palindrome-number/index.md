---
title: "9. Palindrome Number"
---

<div class="problem-header">
  <div class="problem-number">9</div>
  <div>
    <div><strong>Palindrome Number</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Math</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))
```

<div class="navigation">
  <a class="prev" href="../reverse-integer/">Anterior</a>
  <a class="next" href="../container-with-most-water/">Siguiente</a>
</div>
