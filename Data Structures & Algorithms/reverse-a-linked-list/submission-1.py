# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Input: head of the Linked List
        Output: New head of the Reversed Linked List
        Edge Case: Empty Linked List, Single Element Linked List
        Plan:
            - Have two temp variables to keep track of next el and the link to its next el
            - Iterate using while loop until temp2 is not null
            - Store temp1.next in temp2
            - update the next for temp1 and make it point to head
            - Move all ptrs to next place
            - Return the head
        """
        """# Edge Cases
        if not head:
            return None
        if not head.next:
            return head
        
        # Variable Declaration
        temp1 = head.next
        temp2 = temp1.next

        # Main Logic
        head.next = None
        while temp1:
            temp1.next = head
            head = temp1
            temp1 = temp2
            if temp2:
                temp2 = temp2.next

        return head
        """

        """RECURSIVE APPROACH"""
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
