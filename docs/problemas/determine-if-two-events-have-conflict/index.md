---
title: "2446. Determine if Two Events Have Conflict"
---

<div class="problem-header">
  <div class="problem-number">2446</div>
  <div>
    <div><strong>Determine if Two Events Have Conflict</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Array, String</div>
  </div>
</div>

## Solución (Python)

```python
class Solution(object):
    def haveConflict(self, event1, event2):
        start1= self.conversion(event1[0])
        end1 = self.conversion(event1[1])
        start2 = self.conversion(event2[0])
        end2 = self.conversion(event2[1])

        return (start1 <= start2 <= end1) or (start2 <= start1 <= end2) 

    def conversion(self, time_str):
        hours, minutes = time_str.split(":")
        h = int(hours)
        m = int(minutes)
        return h*60 + m

sol = Solution()
print(sol.haveConflict(["01:15","02:00"], ["02:00","03:00"]))
print(sol.haveConflict(["01:00","02:00"], ["01:20","03:00"]))
print(sol.haveConflict(["10:00","11:00"], ["14:00","15:00"]))
```

<div class="navigation">
  <a class="prev" href="../number-of-laser-beams-in-a-bank/">Anterior</a>
  <a class="next" href="../minimum-operations-to-make-the-integer-zero/">Siguiente</a>
</div>
