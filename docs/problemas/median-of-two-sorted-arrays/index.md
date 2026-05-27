---
title: "4. Median of Two Sorted Arrays"
---

<div class="problem-header">
  <div class="problem-number">4</div>
  <div>
    <div><strong>Median of Two Sorted Arrays</strong> <span class="badge-hard">Hard</span></div>
    <div><strong>Tags:</strong> Array, Binary Search, Divide and Conquer</div>
  </div>
</div>

## Solución (Python)

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2
        left = (n1 + n2 + 1) // 2
        low, high = 0, n1
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
        #antepenultimo
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')

            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            #penultimo
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
            #ultimo segmento
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return 0




s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))            # 2.0
print(s.findMedianSortedArrays([1, 2], [3, 4]))         # 2.5
print(s.findMedianSortedArrays([1, 3, 8], [2, 5, 9]))   # 4.0
```

<div class="navigation">
  <a class="prev" href="../longest-substring-without-repeating-characters/">Anterior</a>
  <a class="next" href="../longest-palindromic-substring/">Siguiente</a>
</div>
