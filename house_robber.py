class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [8, 0, 1, 3]
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        t = [nums[i] for i in range(len(nums))]
        t[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            t[i] = max(t[i-1], nums[i]+t[i-2])
            
        return t[-1]
        
        # total[i] = t[i-1] + nums[i] + t[i-2] 
        # t[0] = nums[0]
        # t[1] = max(t[0], nums[1])
        # t[2] = max(t[1], nums[2] + t[0])
        # t[3] = max(t[2], nums[3] + t[1])
