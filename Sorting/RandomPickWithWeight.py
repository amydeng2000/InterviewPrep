import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.freq = [w[0]]
        for i in range(1, len(w)):
            self.freq.append(self.freq[-1]+w[i])
        

    def pickIndex(self):
        """
        :rtype: int
        """
        num = random.randrange(1, self.freq[-1]+1)
        return self.search(num)
    
    def search(self, num):
        low = 0
        high = len(self.freq)-1
        while low < high:
            mid = low + (high - low) //2
            if self.freq[mid] >= num: high = mid
            else: low = mid+1
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()