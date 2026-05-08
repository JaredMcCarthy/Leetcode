---
title: "3. Longest Substring Without Repeating Characters"
---

<div class="problem-header">
  <div class="problem-number">3</div>
  <div>
    <div><strong>Longest Substring Without Repeating Characters</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Hash Table, Sliding Window, String</div>
  </div>
</div>

## Solución (Python)

```python


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ventana = set()
        max_longitud = 0
        inicio = 0

        for fin in range(len(s)):
            while s[fin] in ventana:
                ventana.remove(s[inicio])
                inicio += 1
            
            ventana.add(s[fin])
            max_longitud = max(max_longitud, fin - inicio + 1)
        
        return max_longitud


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
```

<div class="navigation">
  <a class="prev" href="../add-two-numbers/">Anterior</a>
  <a class="next" href="../longest-palindromic-substring/">Siguiente</a>
</div>
