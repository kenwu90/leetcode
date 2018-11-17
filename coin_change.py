class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 0

        result = [False for i in range(amount+1)]
        result[0] = 0
        buf = [0]
        cnt = 0
        while len(buf) > 0:
            new_buf = []
            print(buf)
            for b in buf:
                for c in coins:

                    if b+c > amount:
                        continue
                    else:

                        if not result[b+c]:
                            result[b+c] = result[b] + 1
                            if b+c == amount:
                                return result[b+c]
                            new_buf.append(b+c)

            buf = new_buf

        return -1


if __name__ == '__main__':
    s = Solution()
    s.coinChange([1, 2, 5], 100)