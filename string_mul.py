class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1 = [ord(n) - ord('0') for n in num1]
        num2 = [ord(n) - ord('0') for n in num2]

        result = 0
        for i in range(len(num1)):
            tmp = 0
            c = 0
            for j in range(len(num2)):
                s = num1[-i - 1] * num2[-j - 1] + c
                tmp += ((10 ^ j) * (s % 10))
                c = int(s / 10)

            tmp += c * (10 ^ len(num2))
            result += (10 ^ i) * tmp

        return str(result)

if __name__ == '__main__':
    s = Solution()
    print(s.multiply('2', '3'))