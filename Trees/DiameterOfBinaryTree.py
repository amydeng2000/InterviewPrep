# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = []
        self.postorder(paths, root)
        return max(paths)
        
    def postorder(self, paths, root):
        if not root:
            paths.append(0)
            return 0
        left = self.postorder(paths, root.left)
        right = self.postorder(paths, root.right)
        paths.append(left + right)
        return max(left, right) + 1