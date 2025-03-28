#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
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



#{ 
 # Driver Code Starts
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        llist = LinkedList()
        values = input().strip().split()
        for i in reversed(values):
            llist.push(int(i))  # Convert input to integers
        llist.head = Solution().removeDuplicates(llist.head)
        llist.printList()
        t -= 1
        print("~")

# } Driver Code Ends