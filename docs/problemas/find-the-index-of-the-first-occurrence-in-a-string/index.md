---
title: "28. Find the Index of the First Occurrence in a String"
---

<div class="problem-header">
  <div class="problem-number">28</div>
  <div>
    <div><strong>Find the Index of the First Occurrence in a String</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> String, String Matching, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def strStr(self, haystack, needle):
        if needle==" ":
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    if haystack[i:i+len(needle)] == needle:
                        return i
            return -1

sol = Solution()
print(sol.strStr("SADBUTSAD", "SAD"))
print(sol.strStr("leetcode", "leeto"))
```

<div class="navigation">
  <a class="prev" href="../remove-element/">Anterior</a>
  <a class="next" href="../search-in-rotated-sorted-array/">Siguiente</a>
</div>
