# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = l1
        res1 = ""
        while curr:
            res1+=str(curr.val)
            curr = curr.next
        res1 =  int(res1[::-1])

        curr = l2
        res2 = ""
        while curr:
            res2+=str(curr.val)
            curr = curr.next
        res2 =  int(res2[::-1])

        res = res1+res2
        
        dummy = ListNode(0)
        ptr =  dummy
        for val in str(res)[::-1]:
            new = ListNode(int(val))
            temp = ptr.next
            ptr.next = new
            ptr = new
        
        return dummy.next

