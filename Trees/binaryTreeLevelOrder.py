# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        paths = [[]]
        return self.traversal(root, paths, 0)
        
    def traversal(self, root, paths, level):
        if not root:
            return
        if level >= len(paths):
            paths.append([])
        paths[level].append(root.val)
        self.traversal(root.left, paths, level+1)
        self.traversal(root.right, paths, level+1)
        return paths
            