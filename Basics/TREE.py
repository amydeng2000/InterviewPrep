# CLARIFYING QUESTIONS
"""
- tree or binary search tree?
- Can the BST have duplicate values? If so, should it be on the left or right of the parent node?
"""

# DEFINITIONS
"""
- Complete BT: every level is fully filled, last level is filled from left to right
- Full BT: no 1 child nodes
- Perfect BT: complete and full
"""

# TRAVERSAL
"""
- Preorder: node, left child, right child
- Inorder: left child, node, right child
- Postorder: left child, right child, node
"""

# TRICKS
"""
- how to keep a nonlocal variable that every recursive call can mutate/add to? 
    - do self.var =  
    - Lists are default to be nonlocal 
"""

class Node:
    def __init__(val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(node):
    if node:
        visit(node)  # do something to the node
        preorder(node.left)
        preorder(node.right)