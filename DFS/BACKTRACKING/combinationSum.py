class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # backtracking prob b/c we need to return the path
        # recursive: take current (target minus) and continue w the same candidates or skip current and move on with the rest of the candidates
        # base cases: if target == 0: append to res array; if target < 0: return
        
        res = []
        def helper(candidates, target, path):
            if target == 0:
                res.append(path)
                return
            if target < 0 or not candidates: return
            helper(candidates, target - candidates[0], path+[candidates[0]])
            helper(candidates[1:], target, path)
            return
        helper(candidates, target, [])
        return res