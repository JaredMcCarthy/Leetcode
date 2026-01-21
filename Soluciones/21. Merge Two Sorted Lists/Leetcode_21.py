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