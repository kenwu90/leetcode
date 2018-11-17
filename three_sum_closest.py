class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        m_dist = abs(nums[0] + nums[1] + nums[2] - target)
        m_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)):

            _target = target - nums[i]
            _nums = [nums[j] for j in range(len(nums)) if i != j]
                
            s = 0
            e = len(_nums) - 1
            vi = _nums[s] + _nums[e] - _target
            fr_left = None
            
            while s < e:
                if abs((_nums[s] + _nums[e] - _target)) < m_dist:
                    m_dist = abs((_nums[s] + _nums[e] - _target))
                    m_sum = _nums[s] + _nums[e] + nums[i]

                if (_nums[s] + _nums[e] - _target) == 0:
                    return target
                elif (_nums[s] + _nums[e] - _target) < 0:
                    s += 1
                    fr_left = True
                else:
                    e -= 1
                    fr_left = False

            """
            if fr_left is not None:
                if fr_left and abs((_nums[s-1] + _nums[e] - _target)) < m_dist:
                    m_dist = abs((_nums[s-1] + _nums[e] - _target))
                    m_sum = _nums[s-1] + _nums[e] + nums[i]
                    print(nums[i], _nums[s-1], _nums[e], m_sum, m_dist)
                elif not fr_left and abs((_nums[s] + _nums[e+1] - _target)) < m_dist:
                    m_dist = abs((_nums[s] + _nums[e + 1] - _target))
                    m_sum = _nums[s] + _nums[e + 1] + nums[i]
                    print(nums[i], _nums[s], _nums[e+1], m_sum, m_dist)

            if e != s:
                if abs((_nums[s] + _nums[e] - _target)) < m_dist:
                    m_dist = abs((_nums[s] + _nums[e] - _target))
                    m_sum = _nums[s] + _nums[e] + nums[i]
                    print('aaa', nums[i], _nums[s], _nums[e], m_sum, m_dist)
            """

        return m_sum


if __name__ == '__main__':
    t = [1,2,4,8,16,32,64,128]
    # [-4, -1, 1, 2]
    s = Solution()
    print(s.threeSumClosest(t, 82))
