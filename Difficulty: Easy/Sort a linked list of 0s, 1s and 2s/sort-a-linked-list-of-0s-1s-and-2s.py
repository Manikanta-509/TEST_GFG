#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    
    

            
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        
        zero_head=zero_tail=Node(-1)
        one_head=one_tail=Node(-1)
        sec_head=sec_tail=Node(-1)
        
        curr=head
        while curr:
            if curr.data==0:
                zero_tail.next=curr
                zero_tail=zero_tail.next
            elif curr.data==1:
                one_tail.next=curr
                one_tail=one_tail.next
            else:
                sec_tail.next=curr
                sec_tail=sec_tail.next
            curr=curr.next
            
        zero_tail.next=one_head.next if one_head.next else sec_head.next
        one_tail.next=sec_head.next
        sec_tail.next=None
        
        return  zero_head.next if zero_head.next else one_head.next or sec_head.next
        
        

                    
        
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends