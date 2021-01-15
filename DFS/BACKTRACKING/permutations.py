class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # backtracking problem
        # for each number in nums:
        # add to curr, remove that from nums, permuteHelper(nums), pop curr, add to nums
        # if nums empty: append curr to res
        
        
        # SOL1: global current list and nums array
        res = []
        curr = []
        def helper():
            if not nums:
                res.append(curr[:])  # necessary to make a copy
                return
            for i in range(len(nums)):
                n = nums[i]
                nums.remove(n)
                curr.append(n)
                helper()
                curr.pop()   # need to revert the changes for the rest of the for loop
                nums.insert(i, n)  #insert instead of append because sequence matters
            return
        helper()
        return res


        # SOL2: FASTER: pass in nums and curr list as args in helper
        res = []
        def helper(nums, curr):
            if not nums:
                res.append(curr)
                return
            for i in range(len(nums)):
                # pass in new nums and curr without changing it within the for loop
                helper(nums[:i]+nums[i+1:], curr+[nums[i]])
            return
        helper(nums, [])
        return res