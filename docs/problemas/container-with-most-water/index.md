---
title: "11. Container With Most Water"
---

<div class="problem-header">
  <div class="problem-number">11</div>
  <div>
    <div><strong>Container With Most Water</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Array, Greedy, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def maxArea(self, height):
        left_index = 0
        right_index = len(height) - 1
        max_area = 0

        while left_index < right_index:
            width = right_index - left_index
            left_height = height[left_index]
            right_height = height[right_index]

            min_height = min(left_height, right_height)     #same min area and max of the prev code
            area = width * min_height
            max_area = max(area, max_area)

            if left_height <= right_height: #this moves the pointer w a small height
                left_index += 1
            else:
                right_index -= 1

        return max_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))
```

<div class="navigation">
  <a class="prev" href="../palindrome-number/">Anterior</a>
  <a class="next" href="../integer-to-roman/">Siguiente</a>
</div>
