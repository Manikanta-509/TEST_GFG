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


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))
        x = int(data[idx + 1].strip())
        idx += 2

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        ob = Solution()
        print(ob.getKthFromLast(head, x))
        t -= 1
        print("~")

# } Driver Code Ends