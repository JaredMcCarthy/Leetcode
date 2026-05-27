---
title: "100. Same Tree"
---

<div class="problem-header">
  <div class="problem-number">100</div>
  <div>
    <div><strong>Same Tree</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Binary Tree, Breadth-First Search, Depth-First Search, Tree</div>
  </div>
</div>

## Solución (Python)

```python

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        
        return (p is not None and q is not None) and (p.val == q.val) and \
            self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

sol = Solution()
print(sol.isSameTree([1,2,3],[1,2,3]))
print(sol.isSameTree([1,2], [1,None,2]))
print(sol.isSameTree([1,2,1], [1,1,2]))
```

<div class="navigation">
  <a class="prev" href="../merge-sorted-array/">Anterior</a>
  <a class="next" href="../symmetric-tree/">Siguiente</a>
</div>
