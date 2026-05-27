---
title: "88. Merge Sorted Array"
---

<div class="problem-header">
  <div class="problem-number">88</div>
  <div>
    <div><strong>Merge Sorted Array</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array, Sorting, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def merge(self, nums1, m, nums2, n):
            i = m - 1
            j = n - 1
            k = m + n - 1
            
            while j >= 0:
                if i >= 0 and nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1

                k -= 1

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(sol.merge([1], 1, [], 0))
print(sol.merge([0], 0, [1], 1))
```

<div class="navigation">
  <a class="prev" href="../remove-duplicates-from-sorted-list/">Anterior</a>
  <a class="next" href="../same-tree/">Siguiente</a>
</div>
