class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 2, -1, -1):

            if nums[i] < nums[i + 1]:
                # found
                tmp = nums[i]
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > tmp:
                        print(i, j, tmp, nums[j])
                        nums[i] = nums[j]
                        nums[j] = tmp
                        break
                print(nums)
                exit()
                s, e = i + 1, len(nums) - 1
                while (s < e):
                    tmp = nums[s]
                    nums[s] = nums[e]
                    nums[e] = tmp
                    s += 1
                    e -= 1

                return

        nums = nums[::-1]
        return

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    s.nextPermutation(nums)
    print(nums)
    exit()
    # 5, 1, 4, 3, 2
    # 5, 1, 3, 4, 2
    s.nextPermutation([5, 1, 3, 4, 2])
    # 5, 1, 4, 2, 3