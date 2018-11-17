
class RecursiveSolution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 0:
            return [[]]
        
        results = self.subsets(nums[:-1])
        new_results = [[n for n in r] for r in results]
        
        for r in new_results:
            r.append(nums[-1])
                
        return results + new_results


class IterativeSolution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]

        results = [[]]
        for i in range(len(nums)):
            new_results = [[n for n in r] for r in results]
            for r in new_results:
                r.append(nums[i])
            results = results + new_results
        return results



if __name__ == "__main__":

    nums = [1, 2, 3]
    s = RecursiveSolution()
    print(s.subsets(nums))

