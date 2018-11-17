class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ''
        for i in range(0, len(s), 2*k):
            substr = s[i:i+k][::-1]
            
            if i+k < len(s):
                substr += s[i+k:i+2*k]
                
            result += substr
            
        return result


def main():
  s = Solution()
  s.reverseStr('abcdefg', 2)


if __name__ == '__main__':
    main()
