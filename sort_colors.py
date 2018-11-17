class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        idx_1 = 0
        idx_2 = l-1
        
        while idx_1 < l and nums[idx_1] == 0:
            idx_1 += 1
            
        while idx_2 > 0 and nums[idx_2] == 2:
            idx_2 -= 1
            
        if idx_1 >= idx_2:
            return nums
        
        i = idx_1
        #print(nums)

        
        while i <= idx_2:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i] = nums[idx_1]
                nums[idx_1] = 0
                idx_1 += 1
                i = max(idx_1+1, i)
            elif nums[i] == 2:
                nums[i] = nums[idx_2]
                nums[idx_2] = 2
                idx_2 -= 1

            print(nums, i, idx_1, idx_2)

def main():
    nums = [2,0,2,1,1,0]
    s = Solution()
    s.sortColors(nums)


if __name__ == '__main__':
    main()