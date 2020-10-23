# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        inleft = self.exist(root.left, p) and self.exist(root.left, q)
        inright = self.exist(root.right, p) and self.exist(root.right, q)
        if inleft: return self.lowestCommonAncestor(root.left, p, q)
        if inright: return self.lowestCommonAncestor(root.right, p, q)
        return root.val
    
    # check if both p, q are in the subtree
    def exist(self, root, p):
        if not root: return False
        if root.val == p: return True
        return self.exist(root.left, p) or self.exist(root.right, p)


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)

s = Solution()
print(s.lowestCommonAncestor(root, 5, 1))