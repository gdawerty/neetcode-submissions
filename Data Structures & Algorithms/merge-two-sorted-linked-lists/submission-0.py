# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        curr3 = ListNode()
        dummy = curr3
        while curr1 or curr2:
            if curr1 and curr2 and curr1.val < curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            elif curr1 and curr2 and curr2.val < curr1.val:
                curr3.next = curr2
                curr2 = curr2.next
            elif curr1:
                curr3.next = curr1
                curr1 = curr1.next
            elif curr2:
                curr3.next = curr2
                curr2 = curr2.next
            curr3 = curr3.next

        return dummy.next
