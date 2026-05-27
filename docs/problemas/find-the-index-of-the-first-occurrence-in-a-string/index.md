---
title: "28. Find the index of the First occurrence in a string"
---

<div class="problem-header">
  <div class="problem-number">28</div>
  <div>
    <div><strong>Find the index of the First occurrence in a string</strong> <span class="badge-easy">Easy</span></div>
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
print(sol.strStr("sadbutsad", "sad"))
print(sol.strStr("leetcode", "leeto"))
```

<div class="navigation">
  <a class="prev" href="../remove-element/">Anterior</a>
  <a class="next" href="../next-permutation/">Siguiente</a>
</div>
