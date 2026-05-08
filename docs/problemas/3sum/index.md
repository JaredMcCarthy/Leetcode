---
title: "15. 3Sum"
---

<div class="problem-header">
  <div class="problem-number">15</div>
  <div>
    <div><strong>3Sum</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Array, Sorting, Two Pointers</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def threeSum(self, nums):
            nums.sort()
            resultado = []
            
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
            
                izquierdo = i + 1
                derecho = (len(nums) - 1)

                while izquierdo < derecho:
                    suma = nums[i] + nums[izquierdo] + nums[derecho]

                    if suma == 0:
                        resultado.append([nums[i], nums[izquierdo], nums[derecho]])
                        izquierdo += 1
                        derecho -= 1

                        #evita duplicado lado izquierdo
                        while izquierdo < derecho and nums[izquierdo] == nums[izquierdo -1]:
                            izquierdo += 1
                        
                        #evita duplicado lado derecho
                        while izquierdo < derecho and nums[derecho] == nums[derecho + 1]:
                            derecho -= 1

                    elif suma < 0:
                        izquierdo += 1
            
                    elif suma > 0:
                        derecho -= 1


            return resultado

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,1,1]))
print(sol.threeSum([0,0,0]))
```

<div class="navigation">
  <a class="prev" href="../longest-common-prefix/">Anterior</a>
  <a class="next" href="../3sum-closest/">Siguiente</a>
</div>
