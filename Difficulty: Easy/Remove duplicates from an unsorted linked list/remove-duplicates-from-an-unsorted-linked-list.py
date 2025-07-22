'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    def removeDuplicates(self, head):
        seen=set()
        prev=None
        curr=head
        while curr:
            if curr.data in seen:
                prev.next=curr.next
            else:
                seen.add(curr.data)
                prev=curr
            curr=curr.next
        return head
        # code here
        # return head after editing list