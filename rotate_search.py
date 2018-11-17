
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = int((left + right) / 2)
#            print(left, middle, right)
            if target == nums[middle]:
                return middle
            elif (target > nums[middle]):
                if target >= nums[left] and nums[middle] < nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target <= nums[right] and nums[middle] > nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
                
        return -1

s = Solution()

print(s.search([4,5,6,7,8, 1, 2, 3], 8))
print(s.search([7, 8, 1, 2, 3, 4, 5, 6], 8))
print(s.search([2,3,4,5,6,7,8,9,1],9))
print(s.search([3, 5, 1], 1))
