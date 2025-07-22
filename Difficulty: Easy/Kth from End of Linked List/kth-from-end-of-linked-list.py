#User function Template for python3
'''
    A linked list node has the following structure
    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        # Reverse the linked list
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev is now the head of the reversed list
        current = prev
        count = 1

        # Traverse the reversed list to find the k-th node
        while current:
            if count == k:
                return current.data  # Return the value (data) of the k-th node
            current = current.next
            count += 1

        return -1  # If k is greater than the length of the list

            
            
            
            
        #code here
