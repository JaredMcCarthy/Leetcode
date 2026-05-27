---
title: "83. Remove Duplicates from Sorted List"
---

<div class="problem-header">
  <div class="problem-number">83</div>
  <div>
    <div><strong>Remove Duplicates from Sorted List</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Linked List</div>
  </div>
</div>

## Solución (Python)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        puntero = head

        while puntero and puntero.next:
            if puntero.val == puntero.next.val:
                puntero.next = puntero.next.next
            else:
                puntero = puntero.next
        
        return head

sol = Solution()
print(sol.deleteDuplicates([1,1,2]))
print(sol.deleteDuplicates([1,1,2,3,3]))
```

<div class="navigation">
  <a class="prev" href="../climbing-stairs/">Anterior</a>
  <a class="next" href="../merge-sorted-array/">Siguiente</a>
</div>
