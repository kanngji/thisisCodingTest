# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        nhead = head

        while nhead.next:
            nhead = nhead.next
            n+=1
        
        half = n//2 + n%2
        while half > 0:
            head = head.next
            half -= 1
        
        return head