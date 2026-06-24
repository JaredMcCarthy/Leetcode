
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