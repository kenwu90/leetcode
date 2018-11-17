class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(left, right):

            start, end = -1, -1

            if left > right:
                return start, end

            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
                start, end = binary_search(left, right)
            elif nums[mid] > target:
                right = mid - 1
                start, end = binary_search(left, right)
            else:
                if mid - 1 < left or nums[mid - 1] < target:
                    start = mid
                elif nums[mid - 1] == target:
                    start, _ = binary_search(left, mid - 1)

                if mid + 1 > right or nums[mid + 1] > target:
                    end = mid
                elif nums[mid + 1] == target:
                    _, end = binary_search(mid + 1, right)

            return start, end

        left, right = 0, len(nums) - 1
        return binary_search(left, right)