class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        cnt_dict = {}

        for n in tasks:
            if n not in cnt_dict:
                cnt_dict[n] = 0
            cnt_dict[n] += 1

        # tasks[i] = task[i-1] 