---
title: "1437. Check If All 1's Are at Least Length K Places Away"
---

<div class="problem-header">
  <div class="problem-number">1437</div>
  <div>
    <div><strong>Check If All 1's Are at Least Length K Places Away</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array</div>
  </div>
</div>

## Solución (Python)

```python

class solution:
	def BinaryLenght(self, nums, k):
		if k == 0:
			return True

		n = len(nums)
		curr = 0
		next = 1

		while curr < n and next < n:
			if nums[next] == 1:
				if nums[curr] == 1 and next - curr <= k:
					return False
				curr = next
			next += 1

		return True

nums1 = [1,0,0,0,1,0,0,1]
k1 = 2

nums2 = [1,0,0,1,0,1]
k2 = 2


sol = solution()
print(sol.BinaryLenght(nums1,k1))
print(sol.BinaryLenght(nums2, k2))
























#SOLUCIONES ADICIONALES BTW 39/69 CASES


		 # last_position = float('-inf')

		 # for current, value in enumerate(nums):
		 # 	if value == 1:
		 # 		distance = current - last_position - 1

		 # 		if distance < k:
		 # 			return False

		 # 			last_position = current

		 # return True
```

<div class="navigation">
  <a class="prev" href="../find-first-and-last-position-of-element-in-sorted-array/">Anterior</a>
  <a class="next" href="../find-x-sum-of-all-k-long-subarrays-ii/">Siguiente</a>
</div>
