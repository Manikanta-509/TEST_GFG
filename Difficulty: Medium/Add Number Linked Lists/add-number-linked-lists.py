#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        def reverse_list(head):
            prev = None
            curr = head
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        # Reverse both linked lists
        num1 = reverse_list(num1)
        num2 = reverse_list(num2)

        dummy = Node(0)
        curr = dummy
        carry = 0

        # Perform addition
        while num1 or num2 or carry:
            val1 = num1.data if num1 else 0
            val2 = num2.data if num2 else 0
            total = val1 + val2 + carry  # Sum of two digits + carry

            carry = total // 10  # Compute carry
            curr.next = Node(total % 10)  # Store single digit in new node
            curr = curr.next  # Move forward in result list

            # Move input list pointers
            num1 = num1.next if num1 else None
            num2 = num2.next if num2 else None

        # Reverse the final sum to maintain the correct order
        result = reverse_list(dummy.next)

        # Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next

        return result 
            
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends