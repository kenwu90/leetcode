class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        num = sum([int(i)*int(i) for i in str(n)])
        s = {1}
        while num not in s:
            s.add(num)
            num = sum([int(i)*int(i) for i in str(num)])
            
        if num == 1:
            return True
        else:
            return False


def main():
  s = Solution()
  print(s.isHappy(2))



if __name__ == '__main__':
    main()
