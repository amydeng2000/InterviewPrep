class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        i = 0
        while i < len(prices)-1:
            print(i)
            while i < len(prices)-1 and prices[i+1] < prices[i]:
                i += 1
            valley = prices[i]
            print("valley:{0}".format(valley))
            while i < len(prices)-1 and prices[i+1] > prices[i]:
                i += 1
            peak = prices[i]
            print("peak:{0}".format(peak))
            total += peak - valley
        return total
        
        
        