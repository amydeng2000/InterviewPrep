# Recursive Solution
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        for n in nums:
            s += n
        if s % 2 != 0: return False
        memo = {}
        return self.helper(nums, 0, s//2, memo)
        
    def helper(self, nums, i, s, memo):
        if s == 0: return True
        if i >= len(nums): return False
        for k in range(i, len(nums)):
            if (k, s) in memo:
                return memo[(k, s)]
        memo[(i, s)] = self.helper(nums, i+1, s-nums[i], memo) or self.helper(nums, i+1, s, memo)
        return memo[(i, s)]


# Iterative approach
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        for n in nums:
            s += n
        if s % 2 != 0: return False
        s /= 2
        memo = [[False for j in range(s+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            memo[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, s+1):
                memo[i][j] = memo[i-1][j]
                if j-nums[i-1] >= 0:
                    memo[i][j] = memo[i][j] or memo[i-1][j-nums[i-1]]
        return memo[len(nums)][s]