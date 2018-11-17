import time


class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """

        next_dict = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        cnt = [1] * 10

        for _ in range(N - 1):
            nxt = [0] * 10
            for j in next_dict:
                for n in next_dict[j]:
                    nxt[n] += cnt[j]
            cnt = nxt

        return sum(cnt) % (1000000000 + 7)


if __name__ == '__main__':
    st = time.time()
    cache = [[0 for j in range(5000)] for i in range(10)]

    #s = Solution()
    #print(s.knightDialer(3797))
    print(time.time()-st)
    #print(s.knightDialer(4))
    #print(s.knightDialer(5))