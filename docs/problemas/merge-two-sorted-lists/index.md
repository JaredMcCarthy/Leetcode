---
title: "21. Merge Two Sorted Lists"
---

<div class="problem-header">
  <div class="problem-number">21</div>
  <div>
    <div><strong>Merge Two Sorted Lists</strong> <span class="badge-easy">Easy</span></div>
    <div><strong>Tags:</strong> Linked List, Recursion</div>
  </div>
</div>

## Solución (Python)

```python
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            tail.next = ListNode()
            tail = tail.next

            if list1 < list2:
                tail = list1
                list1 = list1.next
            else:
                tail = list2
                list2 = list2.next

        tail.next = list1 or list2

        return dummy.next

sol = Solution()
print(sol.mergeTwoLists([1,2,4], [1,3,4]))
```

<div class="navigation">
  <a class="prev" href="../valid-parentheses/">Anterior</a>
  <a class="next" href="../remove-duplicates-from-sorted-array/">Siguiente</a>
</div>
