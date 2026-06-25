
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.comparar(root.left, root.right)

    def comparar(self, nodoA, nodoB):
        if nodoA is None and nodoB is None:
            return True
        if nodoA is None or nodoB is None:
            return False
        if nodoA.val != nodoB.val:
            return False
        return self.comparar(nodoA.left, nodoB.right) and self.comparar(nodoA.right, nodoB.left)

sol = Solution()
print(sol.comparar([1,2,2,3,4,4,3]))
print(sol.comparar([1,2,2,None,3,None,3]))