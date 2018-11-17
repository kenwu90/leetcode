class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        results = []
        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            _nums = nums[i+1:]

            l = 0
            r = len(_nums) - 1

            while l < r:
                s = _nums[l] + _nums[r]

                if s == -nums[i]:
                    results.append([nums[i], _nums[l], _nums[r]])
                    l += 1
                    while l < r and (_nums[l] == _nums[l-1]):
                        print(l)
                        l += 1
                elif s > -nums[i]:
                    r -= 1
                else:
                    l += 1

        return results

if __name__ == '__main__':
    s = Solution()
    c = [-1,0,1,2,-1,-4]
    s.threeSum(c)