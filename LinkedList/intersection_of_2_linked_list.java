/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode new_list(ListNode headA, ListNode headB)
    {
        ListNode temp1 = headA;
        ListNode temp2 = headB;
        ListNode headC = temp1;
        if(headA == null || headB == null)
        {
            return null;
        }
        while(temp1.next != null)
        {
            temp1=temp1.next;
        }
        headC.next = headB;
        return headC;
    }
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode headC = new_list(headA, headB);
        ListNode curr  = headC;
        ListNode runner = headC;
        while(curr != null)
        {
            runner = curr;
            while(runner.next !=null)
                if(curr.val == runner.next.val)
                {
                    return(curr);
                }
                else
                {
                    runner = runner.next;
                }
            curr = curr.next;
        }
        return(null);

    }
}