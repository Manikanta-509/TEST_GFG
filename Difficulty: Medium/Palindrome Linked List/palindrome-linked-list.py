#User function Template for python3
'''

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        left, right = head, prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True
