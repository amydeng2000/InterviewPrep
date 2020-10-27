class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxDiff = 0
        valley = prices[0]
        for p in prices:
            if p-valley > maxDiff:
                maxDiff = p-valley
            elif p < valley:
                valley = p
        reutrn maxDiff