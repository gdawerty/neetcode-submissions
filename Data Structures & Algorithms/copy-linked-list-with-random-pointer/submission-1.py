"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #create copies of all the nodes, create a hash map so that we can map the random nodes, then assign the random nodes after
        if not head:
            return None

        old_to_new = {}

        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while curr:
            clone = old_to_new[curr]
            clone.next = old_to_new.get(curr.next)
            clone.random = old_to_new.get(curr.random)
            
            curr = curr.next

        return old_to_new[head]