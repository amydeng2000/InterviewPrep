class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        longest = 0
        for i in range(len(nums)):
            maxlen = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    maxlen = max(dp[j]+1, maxlen)
            dp[i] = maxlen
            if maxlen > longest: longest = maxlen
        return longest