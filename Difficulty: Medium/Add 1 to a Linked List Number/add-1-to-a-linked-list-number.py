#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self, head):
        # Helper function to reverse the linked list
        def reverse_list(head):
            prev = None
            curr = head
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        # Step 1: Reverse the linked list
        head = reverse_list(head)
        
        # Step 2: Add 1 to the reversed list
        curr = head
        carry = 1  # We need to add 1
        prev = None
        
        while curr:
            new_value = curr.data + carry
            carry = new_value // 10  # Compute the carry for next iteration
            curr.data = new_value % 10  # Store the digit (mod 10)
            prev = curr  # Move prev pointer
            curr = curr.next  # Move to next node
            
            if carry == 0:
                break
        
        # If there's still carry left, add a new node
        if carry:
            prev.next = Node(carry)
        
        # Step 3: Reverse the list back to original order
        return reverse_list(head)
            
            
    
            
        #Returns new head of linked List.

        #Returns new head of linked List.