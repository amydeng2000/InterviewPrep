class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        lastGood = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= lastGood:
                lastGood = i
        return lastGood == 0
        
    
            
        
        
        