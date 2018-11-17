class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        pre_map = {}
        for pre, cur in prerequisites:
            if cur not in pre_map:
                pre_map[cur] = []
            pre_map[cur].append(pre)

        check = [False for i in range(numCourses)]
        buf = []

        def dfs(c):
            print(buf, c)
            if c in buf:
                return True
            else:
                buf.append(c)
                if c in pre_map:
                    for next_c in pre_map[c]:
                        check[next_c] = True
                        with_loop = dfs(next_c)
                        if with_loop:
                            return True

                buf.pop()
                return False

        for cur in range(numCourses):
            if check[cur]:
                continue

            check[cur] = True
            with_loop = dfs(cur)

            if with_loop:
                return False

        return True



if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[0, 1], [1, 0]]))