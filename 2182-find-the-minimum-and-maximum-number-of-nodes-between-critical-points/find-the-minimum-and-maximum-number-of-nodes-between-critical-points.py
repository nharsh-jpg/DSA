# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        pos=1
        first=-1
        last=-1
        minDist=float('inf')
        while curr.next:
            nxt=curr.next
            pos+=1
            if (curr.val>prev.val and curr.val>nxt.val) or \
               (curr.val<prev.val and curr.val<nxt.val):
                if first==-1:
                    first=pos
                else:
                    minDist=min(minDist,pos-last)
                last=pos
            prev=curr
            curr=nxt
        if first==last:
            return [-1, -1]
        maxDist=last-first
        return [minDist,maxDist]