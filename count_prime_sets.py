class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        
        prime_sets = set([2, 3, 5, 7, 11, 13, 17, 19])
        
        a = 0
        for i in range(L, R+1):
            c = 0
            while i:
                i &= (i-1)
                c += 1
            if c in prime_sets:
                a += 1
                
        return a


s = Solution()
print(s.countPrimeSetBits(842, 888))
