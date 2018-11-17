
nums = [0, 1, 0, 3, 12]
zero_index = 0
non_zero_index = 0


    # find first zero
    while zero_index < len(nums) and nums[zero_index] != 0:
        zero_index += 1

    # find fisrt non-zero
    while non_zero_index < len(nums) and nums[non_zero_index] == 0:
        non_zero_index += 1

    print(zero_index, non_zero_index)
    # swap if non_zero_index > zero_index
    if zero_index < len(nums) and non_zero_index < len(nums) and non_zero_index > zero_index:
        tmp = nums[non_zero_index]
        nums[non_zero_index] = nums[zero_index]
        nums[zero_index] = tmp


