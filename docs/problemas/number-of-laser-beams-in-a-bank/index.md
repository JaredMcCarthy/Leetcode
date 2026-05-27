---
title: "2125. Number of Laser beams in a Bank"
---

<div class="problem-header">
  <div class="problem-number">2125</div>
  <div>
    <div><strong>Number of Laser beams in a Bank</strong> <span class="badge-medium">Medium</span></div>
    <div><strong>Tags:</strong> Array, Math, Matrix, String</div>
  </div>
</div>

## Solución (Python)

```python

class Solution(object):
    def numberOfBeams(self, bank):
        res = int(0)
        ultimolaser = int(0)
        n = len(bank[0])

        for i in range(len(bank)):
            conteolaser = 0
            for j in range(len(bank[i])):
                if bank[i][j] == '1':
                    conteolaser += 1

            if conteolaser > 0:
                if ultimolaser != 0:
                    res += ultimolaser * conteolaser
                ultimolaser = conteolaser
        
        return res

sol = Solution()
print(sol.numberOfBeams(["011001","000000","010100","001000"]))
print(sol.numberOfBeams(["000","111","000"]))
```

<div class="navigation">
  <a class="prev" href="../finding-3-digit-even-numbers/">Anterior</a>
  <a class="next" href="../determine-if-two-events-have-conflict/">Siguiente</a>
</div>
