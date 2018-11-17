class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return -1
        
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = int(n / 10)
            
        buffer = [digits[0]]
        
        for i in range(1, len(digits)):
            if digits[i] < buffer[-1]:
                
                k = -1
                while(-k < len(buffer) and buffer[k-1] > digits[i]):
                    k -= 1
                
                tmp = buffer[k]
                buffer[k] = digits[i]
                digits[i] = tmp
                digits[:i] = sorted(buffer, reverse=True)
                r = 0
                for j in range(len(digits)-1, -1, -1):
                    r *= 10
                    r += digits[j]
                return r if r < 2147483648 else -1
            else:
                buffer.append(digits[i])
                
        return -1
