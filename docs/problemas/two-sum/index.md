---
title: "1. Two Sum"
---

<div class="problem-header">
  <div class="problem-number">1</div>
  <div>
    <div><strong>Two Sum</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array, Hash Table</div>
  </div>
</div>

## Solución (Python)

```python


# No nos pide un orden en los elementos.
# La lista ya esta ordenada.


class solution:
	def twosum(self, nums, target):
		for i in range(len(nums)):
			for j in range(len(nums)):
				if i == j:
					continue
				elif nums[i] + nums[j] == target:
					return [i, j]



nums1 = [2, 7, 11, 15]
target1 = 9


nums2 = [3, 2, 4]
target2 = 6


nums3 = [3, 3]
target3 = 6


sol = solution()
print(sol.twosum(nums1, target1	))
print(sol.twosum(nums2, target2	))
print(sol.twosum(nums3, target3	))
```

<div class="navigation">
  <span></span>
  <a class="next" href="../add-two-numbers/">Siguiente</a>
</div>
