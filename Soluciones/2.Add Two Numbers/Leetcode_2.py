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