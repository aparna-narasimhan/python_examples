'''
Leetcode (Python): Linked List Cycle
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?
Solution:
Using a fast pointer that advances two nodes each time and a slow pointer that advances on node, we always detect a cycle as the fast pointer cannot overtake the slow one without being in the same node in one of the ``turns".
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fastPointer = head
        slowPointer = head
        while fastPointer != None and fastPointer.next != None:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                return True
        return False