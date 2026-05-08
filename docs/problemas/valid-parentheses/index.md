---
title: "20. Valid Parentheses"
---

<div class="problem-header">
  <div class="problem-number">20</div>
  <div>
    <div><strong>Valid Parentheses</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Stack, String</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = { ")": "(", "]" : "[",  "}" : "{" }

        for c in s:
            if c in closeToOpen:   # 'in' porque queremos saber si c esa en sus yaves
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
print(sol.isValid("([)]"))
```

<div class="navigation">
  <a class="prev" href="../4sum/">Anterior</a>
  <a class="next" href="../merge-two-sorted-lists/">Siguiente</a>
</div>
