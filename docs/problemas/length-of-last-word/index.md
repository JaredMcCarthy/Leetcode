---
title: "58. Length of Last Word"
---

<div class="problem-header">
  <div class="problem-number">58</div>
  <div>
    <div><strong>Length of Last Word</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> String</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split()
        if word:
            lastword = word[-1]
            return len(lastword)
        else:
            return 0

sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("luffy is still joyboy"))
```

<div class="navigation">
  <a class="prev" href="../permutations/">Anterior</a>
  <a class="next" href="../plus-one/">Siguiente</a>
</div>
