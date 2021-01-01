class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # + number of ways that target-n can be summed up for each n in nums
        # dp[i] = number of ways to sum up to amount i
        # base cases: target == 0, 1; target < 0: 0; check cache
        
        
        dp = [-1] * (target+1)
        def combSum(target):
            if target == 0: return 1
            if target < 0: return 0
            if dp[target] >= 0: return dp[target]
            total = 0
            for n in nums:
                total += combSum(target-n)
            dp[target] = total
            return total
        return combSum(target)