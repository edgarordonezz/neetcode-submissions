/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        // 1st
        // 0 -> 1 -> 2 -> 3 -> null
        // c    t
        // 0 -> 1 -> 2 -> 3 -> null
        // n    c
        // 0 -> 1 -> 2 -> 3 -> null
        // p    c

        // 2nd
        // 0 -> 1 -> 2 -> 3 -> null
        // c    t
        // 0 -> 1 -> 2 -> 3 -> null
        // n    c
        // 0 -> 1 -> 2 -> 3 -> null
        // p    c
        ListNode curr = head;
        ListNode prev = null;

        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = prev; // points to null now
            prev = curr;
            curr = temp;
        }
        return prev;
    }
}
