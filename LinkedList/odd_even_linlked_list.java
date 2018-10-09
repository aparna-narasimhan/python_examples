/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
 */

class Solution {
    public static ListNode last_node=null;
    public ListNode oddEvenList(ListNode head) {
        ListNode t = head;
        if(head == null)
        {
            return head;
        }
        get_last_node(head);
        ListNode first_even = head.next;
        while(true)
        {
            ListNode temp = t.next;
            last_node.next = temp;
            t.next = temp.next;
            t = t.next;
            last_node = temp;
            last_node.next = null;
            if(t.next == first_even)
                break;

        }
        return(head);
    }

    public void get_last_node(ListNode head)
        {
        ListNode temp;
        temp = head;
        while(temp.next != null)
            {
            temp=temp.next;
            }
        last_node = temp;
        }

}