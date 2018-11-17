class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        #sorted_people = sorted(sorted_people, key=lambda x: x[0], reverse=True)
        for i in range(1, len(sorted_people)):
            print(sorted_people[i], i)
            if sorted_people[i][1] < i:
                tmp = sorted_people.pop(i)
                print(sorted_people)
                sorted_people.insert(tmp[1], tmp)
                print(sorted_people)

        return sorted_people


def main():
    s = Solution()
    print(s.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))


if __name__ == '__main__':
    main()