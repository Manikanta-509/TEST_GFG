'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''


class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head
        
        # Create dummy nodes for 0, 1, 2 lists
        zeroD = Node(0)
        oneD = Node(0)
        twoD = Node(0)
        
        # Tails for the three lists
        zero = zeroD
        one = oneD
        two = twoD
        
        # Traverse and distribute nodes into 0s, 1s, 2s lists
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:  # curr.data == 2
                two.next = curr
                two = two.next
            curr = curr.next
        
        # Connect the three lists
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None   # end of list
        
        # New head is the first non-empty list
        return zeroD.next

        #code here
    