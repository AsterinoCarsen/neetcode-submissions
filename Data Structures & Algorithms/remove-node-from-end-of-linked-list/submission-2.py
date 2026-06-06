# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        outHead = head

        while head:
            length += 1
            head = head.next
        
        indexToRemove = length - n
        head = outHead
        for i in range(indexToRemove - 1):
            head = head.next

        if indexToRemove == 0:
            return outHead.next

        if (indexToRemove - 1) == length:
            head.next = None
        else:
            head.next = head.next.next

        return outHead
        