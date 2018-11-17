import sys

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
       
        # find leading 1
        a = num
        cnt = 0
        while ((a & sys.maxsize) > 0):
            cnt += 1
            a = a >> 1
           
        b = 0
        for i in range(cnt):
            b = b | 1
            b = b << 1
        b = b >> 1
        return (num ^ b)


def main():

    s = Solution()
    print(s.findComplement(5))

 

if __name__ == '__main__':
    main()
   
