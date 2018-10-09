# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        is_empty = True
        l3 = None
        temp = None
        while l1 and l2:
            if(l1.val < l2.val):
                if is_empty:
                    l3 = ListNode(l1.val)
                    temp = l3
                    is_empty = False
                else:
                    if temp:
                        temp.next = ListNode(l1.val)
                        temp = temp.next
                l1 = l1.next
            else:
                if is_empty:
                    l3 = ListNode(l2.val)
                    temp = l3
                    is_empty = False
                else:
                    if temp:
                        temp.next = ListNode(l2.val)
                        temp = temp.next
                l2 = l2.next
        while l1:
            if temp:
                temp.next = ListNode(l1.val)
                l1 = l1.next
        while l2:
            if temp:
                temp.next = ListNode(l2.val)
                l2 = l2.next
        return l3