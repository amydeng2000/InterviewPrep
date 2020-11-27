class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            if nums[r] == 0:
                n = nums.pop(r)
                nums.insert(0, n)
                l += 1
                r += 1
            elif nums[r] == 2:
                n = nums.pop(r)
                nums.append(n)
            if l < len(nums) and nums[l] == 2:
                n = nums.pop(l)
                nums.append(n)
                l -= 1
                r -= 1
            elif l < len(nums) and nums[l] == 0:
                n = nums.pop(l)
                nums.insert(0, n)
            l += 1
            r -= 1
        return nums

s = Solution()
s.sortColors([2,0,2,1,1,0])