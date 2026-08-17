# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        s = ""
        temp = 0

        curr = ListNode(0)

        dummy = curr

        while l1 or l2:
            if l1 and l2:
                if l1.val + l2.val + carry > 9:
                    temp = (l1.val + l2.val + carry) % 10
                    carry = 1
                else:
                    temp = (l1.val + l2.val + carry) % 10
                    carry = 0
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if l1.val + carry > 9:
                    temp = (l1.val + carry) % 10
                    carry = 1
                else:
                    temp = (l1.val + carry) % 10
                    carry = 0
                l1 = l1.next
            else:
                if l2.val + carry > 9:
                    temp = (l2.val + carry) % 10
                    carry = 1
                else:
                    temp = (l2.val + carry) % 10
                    carry = 0
                l2 = l2.next

            curr.next = ListNode(temp)
            curr = curr.next

        if carry == 1:
            curr.next = ListNode(1)
        
        return dummy.next
            