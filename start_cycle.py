# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        n1 = head
        n2 = head

        if n1 is None or n1.next is None or n1.next.next is None:
            print('wow')
            return None

        n1 = n1.next.next
        n2 = n2.next

        while n1 is not None and n2 is not None and n1.val != n2.val:
            if n1.next is None or n1.next.next is None:
                return None
            else:
                n1 = n1.next.next

            if n2.next is None:
                return None
            else:
                n2 = n2.next

        if n1 is None or n2 is None:
            return None

        n1 = head
        while n1.val != n2.val:
            print(n1.val, n2.val)
            n1 = n1.next
            n2 = n2.next
        print(n1.val, n2.val)
        return n1


if __name__ == '__main__':
    s = Solution()
    l = [-1, -7, 7, -4, 19, 6, -9]
    head = ListNode(l[0])
    cur = head
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next

    st = ListNode(-5)
    st.next = ListNode(-2)
    st.next.next = st

    cur.next = st

    r  = s.detectCycle(head)
    if r is not None:
        print(r.val)
    else:
        print('no cycle')
