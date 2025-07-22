"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        # Reverse first k nodes
        prev = None
        curr = head
        count = 0
        
        # Check how many nodes are available
        temp = head
        total = 0
        while temp:
            total += 1
            temp = temp.next
        
        # Reverse k nodes (or all if less than k remaining)
        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
        
        # Recursively call for the rest of the list
        if curr:
            head.next = self.reverseKGroup(curr, k)
        
        return prev
        
        # Code here