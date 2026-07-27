# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Phase 1: Create a dummy node, and reach left pointer
        dummy =  ListNode(0, head)
        prev = dummy
        curr = head
        n = left -1
        while n > 0 and curr:
            prev = curr
            curr = curr.next
            n-=1

        # Store left_prev to later connect it to right
        left_prev = prev

        # Phase 2: Reverse the [right to left] LL part
        prev = None
        n = (right-left) + 1
        while n > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr =  temp
            n-=1

        # Phase 3:
        # connect left node to right+1 node
        left = left_prev.next
        left.next = curr
        # connect left-1 node to right node
        left_prev.next = prev

        return dummy.next


        

        
        

        