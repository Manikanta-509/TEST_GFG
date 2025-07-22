#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isCircular(self, head):
        if not head:
            return False
        temp=head.next
        while temp is not None and temp!=head:
            temp=temp.next
        return temp==head
        # Code here