class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [-1]*(num+1)
        bits[0] = 0
        for i in range(1, num+1):
            bits[i] = i % 2 + bits[i >> 1]
        return bits
                