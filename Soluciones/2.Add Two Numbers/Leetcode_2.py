class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_node = ListNode(0)
        apuntador = dummy_node
        carry = 0 

        while l1 or l2 or carry > 0:
            valor1 = l1.val if l1 else 0
            valor2 = l2.val if l2 else 0

            suma = valor1 + valor2 + carry
            carry = suma // 10

            apuntador.next = ListNode(suma % 10)
            apuntador = apuntador.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy_node.next
    
if __name__ == "__main__":
    def build_list(nums):
        head = ListNode(nums[0]); cur = head
        for n in nums[1:]:
            cur.next = ListNode(n); cur = cur.next
        return head

    def to_list(node):
        res = []
        while node:
            res.append(node.val); node = node.next
        return res

    sol = Solution()
    l1 = build_list([2,4,3])
    l2 = build_list([5,6,4])
    print(to_list(sol.addTwoNumbers(l1, l2)))  # espera [7,0,8]
