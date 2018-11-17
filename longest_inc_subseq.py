class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        inc_num = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            tmp = []
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmp.append(inc_num[j] + 1)
                else:
                    tmp.append(1)
            inc_num[i] = max(tmp)
        return max(inc_num)

def main():
    s = Solution()
    s.lengthOfLIS([10,9,2,5,3,7,101,18])


if __name__ == '__main__':
    main()