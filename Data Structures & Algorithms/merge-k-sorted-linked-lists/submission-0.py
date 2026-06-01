# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Input: List of linkedlists
        Output: One linked list (merged) with sorted elements from other linked lists
        Edge Cases:
            - Empty List
            - Single Linked List
        Plan:
            - Find the minimum element from all the linked lists
            - Move that to the sorted merged linked list
            - sorted lists last element -> next = currList
            - currList -> next = None
            - pop the front element from the list
        """
        # Edge Cases
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # Main Logic
        head = None # head for the merged list
        curr = None # last Element of the merged list
        while lists:
            # Find Min element from all linked lists
            n = len(lists)
            minNode = lists[0]
            minI = 0
            for i in range (1, n):
                if lists[i].val < minNode.val:
                    minNode = lists[i]
                    minI = i
            
            # Add the Min element to the Final Merged List
            if not head:
                head = minNode
                curr = head
            else:
                curr.next = minNode
                curr = curr.next
            # Remove the Min element from its current list
            if minNode.next:
                lists[minI] = minNode.next
            else:
                lists.pop(minI)
            minNode.next = None
        
        return head
