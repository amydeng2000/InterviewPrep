# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root.left, root.right)
            
        
    def check(self, root1, root2):
        if not (root1 or root2): return True
        if not (root1 and root2): return False
        if root1.val != root2.val: return False
        return self.check(root1.left, root2.right) and self.check(root1.right, root2.left)