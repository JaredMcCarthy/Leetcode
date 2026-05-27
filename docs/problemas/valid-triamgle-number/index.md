---
title: "611. Valid Triamgle Number"
---

<div class="problem-header">
  <div class="problem-number">611</div>
  <div>
    <div><strong>Valid Triamgle Number</strong> <span class="badge-medium">Unknown</span></div>
    <div><strong>Tags:</strong> —</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        contador = 0

        for k in range(len(nums) -1, -1, -1):
            lado_largo = nums[k]

            i = 0
            j = k - 1

            while i < j:
                lado_a = nums[i]
                lado_b = nums[j]

                if lado_a + lado_b > lado_largo:
                    contador += (j - i)
                    j -= 1
                else:
                    i += 1

        return contador

sol = Solution()
print(sol.triangleNumber([2,2,3,4]))
print(sol.triangleNumber([4,2,3,4]))
```

<div class="navigation">
  <a class="prev" href="../power-of-three/">Anterior</a>
  <a class="next" href="../convert-integer-to-the-sum-of-two-no-zero-integers/">Siguiente</a>
</div>
