"""
- when to use DFS? when you need to go down a full path before backtracking
- basically the same as recursion
- dfs() is usually a helper function of the parent function
"""

# General Sturcture of a DFS problem
def parentFunction(grid/arr, param):
    # self.nonLocalInt = 0 instantiated here if needed

    def dfs(x, additionalTrackingElem):
        # out of bounds check (for x or for i,j in grid problems)
        # visited check
        # base cases
        # do sth to x or set visited(x)  -> preorder
        # keep track of non-repeating elements (add to set/list)
        for every neighbor/child of x:
            dfs(child)
            OR if not dfs(child): return False
        # delete non-repeating elements from set/list
        # do sth to x or set visited(x)  -> postorder
        return recursive result

    for every element x in grid/arr:
        dfs(x)
        OR if not dfs(x) return False
        # keep track of counter here if needed
    return True/counter