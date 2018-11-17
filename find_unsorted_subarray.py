class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 1 9 8 6 4 3 10 100 99 101 3 2 1 1 2 3
        
        if len(nums) == 1:
            return 0
        
        m = len(nums) - 1
        M = 0
        max_v = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < max_v:
                M = max(M, i)
                print(m, nums[i]) 
                m = min(i-1, m)
                print(m, nums[i]) 
                
                j = m
                print(nums[j], nums[i], j, i) 
                while j > 0 and nums[j-1] > nums[i]:
                    j -= 1
                    
                m = j
                print(m, nums[i]) 
                
            else:
                max_v = max(max_v, nums[i])
            
        print(M, m)
        return max(M - m + 1, 0)



s = Solution()
a = [2,6,4,8,10,9,15]

s.findUnsortedSubarray(a)
