---
title: "14. Longest Common Prefix"
---

<div class="problem-header">
  <div class="problem-number">14</div>
  <div>
    <div><strong>Longest Common Prefix</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array, String, Trie</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
```

<div class="navigation">
  <a class="prev" href="../roman-to-integer/">Anterior</a>
  <a class="next" href="../3sum/">Siguiente</a>
</div>
