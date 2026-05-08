---
title: "5. Longest Palindromic Substring"
---

<div class="problem-header">
  <div class="problem-number">5</div>
  <div>
    <div><strong>Longest Palindromic Substring</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Dynamic Programming, String, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python


class Solution(object):
    def longestPalindrome(self, s):
        length = len(s) * 2
        index_longest = offset_longest = 0
        for index in range(length):
            offset = 0
            for offset in range(1 + index % 2, min(index, length - index), 2):
                if s[(index - offset) // 2] != s[(index + offset) // 2]:
                    offset -= 2
                    break

            if offset > offset_longest:
                index_longest = index
                offset_longest = offset
        return s[(index_longest - offset_longest) // 2: (index_longest + offset_longest) // 2 + 1] 


if __name__ == "__main__":
	sol = Solution()
	print(sol.longestPalindrome("cbbd"))
	print(sol.longestPalindrome("racecar"))
	print(sol.longestPalindrome("abc"))
```

<div class="navigation">
  <a class="prev" href="../longest-substring-without-repeating-characters/">Anterior</a>
  <a class="next" href="../reverse-integer/">Siguiente</a>
</div>
