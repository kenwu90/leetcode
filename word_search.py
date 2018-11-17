class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(board) == 0 or board[0] == 0:
            return False

        y_len, x_len, w_len = len(board), len(board[0]), len(word)
        if w_len > y_len * x_len:
            return False

        print(y_len, x_len, w_len)

        check = [[False for j in range(x_len)] for i in range(y_len)]

        def search(y, x, c, checked):
            checked[y][x] = True
            if board[y][x] == word[c]:
                if c == w_len - 1:
                    checked[y][x] = False
                    return True
                else:
                    # left
                    next_xy = []

                    next_x, next_y = max(x - 1, 0), y
                    next_xy.append((next_x, next_y))

                    # right
                    next_x, next_y = min(x + 1, x_len - 1), y
                    next_xy.append((next_x, next_y))

                    # down
                    next_x, next_y = x, min(y + 1, y_len - 1)
                    next_xy.append((next_x, next_y))

                    # up
                    next_x, next_y = x, max(y - 1, 0)
                    next_xy.append((next_x, next_y))

                    for next_x, next_y in next_xy:
                        r = search(next_y, next_x, c+1, checked)
                        if r:
                            checked[y][x] = False
                            return True

            checked[y][x] = False
            return False

        for i in range(y_len):
            for j in range(x_len):
                if search(i, j, 0, check):
                    return True

        return False


if __name__:
    s = Solution()
    a = [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
          "a", "a", "a", "a", "a", "a", "a", "b"]]
    st = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s.exist(a, st)
