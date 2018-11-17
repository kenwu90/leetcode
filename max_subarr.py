class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 

        if len(nums) == 0:
            return 0
        
        m = nums[0] # largest so fas
        v = max(0, nums[0]) # new largest candidate
        print(v)
        for i in range(1, len(nums)):
            print(v, nums[i], m)
            t = v + nums[i]
            m = max(m, v)
            
            v = max(t, 0)
            
        return m

s = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]

s.maxSubArray(nums)
