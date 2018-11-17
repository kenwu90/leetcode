class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = [[0 for j in range(len(nums))] for i in range(len(nums))]
        print(result)
        for i in range(len(nums)):
            result[0][i] = nums[i]
            
        max_ = max(result[0])
        
        for i in range(1, len(nums)):
            for j in range(len(nums)-i):
                result[i][j] = result[i-1][j] * nums[i+j]
                print(max_, result[i][j])
                max_ = max(result[i][j], max_)
                
        return max_


if __name__ == '__main__':
    s = Solution()
    s.maxProduct([1, 2, 3, -1, 3])
