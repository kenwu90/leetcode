# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def oddEvenList(self, head):
        # for this, we are talking about the node val instead of the node number
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        even_idx = head
        pre_even_idx = None
        while True:
            # find first even
            while(even_idx is not None and ((even_idx.val % 2) != 0)):
                pre_even_idx = even_idx
                even_idx = even_idx.next
        
            # check valid
            if even_idx is None:
                return head
        
            # find first odd after even
            odd_idx = even_idx.next
            pre_odd_idx = even_idx
            while(odd_idx is not None and ((odd_idx.val % 2) == 0)):
                pre_odd_idx = odd_idx
                odd_idx = odd_idx.next
                
            if odd_idx is None:
                return head
   
            # swap
            if pre_even_idx is not None:
                pre_even_idx.next = odd_idx
            else:
                head = odd_idx
            pre_odd_idx.next = odd_idx.next
            odd_idx.next = even_idx
            pre_even_idx = odd_idx



def main():
    s = Solution()

    head = ListNode(1)

    idx = head

    for i in range(2, 5):
       idx.next = ListNode(i)
       idx = idx.next

    idx = head
    while idx is not None:
        print(idx.val)
        idx = idx.next

    head = s.oddEvenList(head)
    idx = head
    while idx is not None:
        print(idx.val)
        idx = idx.next

if __name__ == '__main__':
    main()


