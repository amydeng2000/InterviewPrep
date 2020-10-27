class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        mem = [-1]*len(nums)
        self.helper(nums, mem, len(nums)-1)
        return max(mem[len(nums)-1], mem[len(nums)-2])
        
    def helper(self, nums, mem, i):
        if i < 0:
            return 0
        if mem[i] < 0:
            mem[i] = max(nums[i]+self.helper(nums, mem, i-2), self.helper(nums, mem, i-1))
        print(mem[i])
        return mem[i]
        