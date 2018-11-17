class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        results = []
        for i in range(len(nums)):
            sub = nums[:i]

            if i < len(nums) - 1:
                sub += nums[i+1:]

            sub_results = self.permute(sub)
            [results.append(sr + [nums[i]]) for sr in sub_results]

        return results


def main():
    s = Solution()
    s.permute([1, 2, 3])


if __name__ == '__main__':
    main()