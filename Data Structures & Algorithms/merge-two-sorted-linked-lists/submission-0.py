# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Input: Head of List1 and List2
        Output: Head of Merged List
        Edge Cases: Both Empty Lists, One Empty List, Single Element List
        Plan: [BRUTE FORCE]
            - Two Iterators, one for each list
            - Check the smaller one and add to new list
            - If one list exhausts: Move all from other list in same order to new list
            - Return head of new list
        """
        # Edge Cases
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Variable Declaration
        itr1 = list1
        itr2 = list2

        # Main Logic
        head = None
        curr = None
        while itr1 and itr2:
            newNode = ListNode(0)
            if head is None:
                head = newNode
            
            if itr1.val <= itr2.val:
                newNode.val = itr1.val
                itr1 = itr1.next
            else:
                newNode.val = itr2.val
                itr2 = itr2.next
            
            if curr is None:
                curr = newNode
            else:
                curr.next = newNode
                curr = curr.next
        
        while itr1:
            newNode = ListNode(itr1.val)
            itr1 = itr1.next
            curr.next = newNode
            curr = curr.next

        while itr2:
            newNode = ListNode(itr2.val)
            itr2 = itr2.next
            curr.next = newNode
            curr = curr.next

        return head
