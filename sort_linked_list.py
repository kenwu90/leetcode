# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cnt = 0
        node = head

        while node is not None:
            cnt += 1
            node = node.next

        def merge_sort(head_node, node_cnt, win_size):

            left_cnt = win_size // 2
            if node_cnt < left_cnt:
                end_node = head_node
                for i in range(node_cnt-1):
                    end_node = end_node.next
                return head_node, end_node
            else:
                dummy = ListNode(-1)
                node = dummy

                right_cnt = node_cnt - left_cnt
                left_node = head_node
                right_node = head_node
                for i in range(left_cnt):
                    right_node = right_node.next

                li, ri = 0, 0

                while li < left_cnt and ri < right_cnt:
                    if left_node.val <= right_node.val:
                        node.next = left_node
                        node = node.next
                        left_node = left_node.next
                        li += 1
                    else:
                        node.next = right_node
                        node = node.next
                        right_node = right_node.next
                        ri += 1

                while li < left_cnt:
                    node.next = left_node
                    node = node.next
                    left_node = left_node.next
                    li += 1

                while ri < right_cnt:
                    node.next = right_node
                    node = node.next
                    right_node = right_node.next
                    ri += 1

                print(dummy.next.val, node.val)
                return dummy.next, node

        win_size = 1
        dummy = ListNode(-1)
        dummy.next = head
        while win_size < cnt:
            win_size *= 2
            node = dummy

            merge_cnt = cnt // win_size

            if merge_cnt * win_size != cnt:
                merge_cnt += 1

            for i in range(merge_cnt):

                before_node = node
                node_cnt = min((i + 1) * win_size, cnt) - i * win_size
                for j in range(node_cnt):
                    node = node.next
                after_node = node.next

                if after_node:
                    print('before, after:', before_node.val, after_node.val)
                else:
                    print('bbbb', before_node.val, after_node)
                s_node, e_node = merge_sort(before_node.next, node_cnt, win_size)
                before_node.next = s_node
                e_node.next = after_node
                node = e_node

        return dummy.next


if __name__ == '__main__':
    s = Solution()

    s_node = ListNode(4)
    node = s_node

    for n in [2, 1, 3]:
        node.next = ListNode(n)
        node = node.next

    node = s.sortList(s_node)

    cnt = 0
    while node:
        print(node.val)
        node = node.next
        cnt += 1
        if cnt >= 10:
            break
