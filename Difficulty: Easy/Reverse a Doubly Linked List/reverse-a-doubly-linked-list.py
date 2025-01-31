#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''
class Solution:
    def reverseDLL(self, head):
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # Store the next node temporarily
            
            curr.next = prev
            curr.prev = next_node
            
            prev = curr
            curr = next_node
        
        return prev  # Return the new head of the reversed DLL




#{ 
 # Driver Code Starts
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = DLLNode(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def printList(head):
    if not head:
        return

    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = DLLNode(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.reverseDLL(head)
        printList(resHead)
        print("~")

# } Driver Code Ends