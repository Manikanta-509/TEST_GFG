#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''
class Solution:
    def findIntersection(self, head1, head2):
        dummy = Node(0)  # Dummy node to store intersection list
        curr = dummy

        while head1 and head2:
            if head1.data == head2.data:  # Matching element found
                curr.next = Node(head1.data)
                curr = curr.next
                head1 = head1.next
                head2 = head2.next
            elif head1.data < head2.data:  # Move head1 forward
                head1 = head1.next
            else:  # Move head2 forward
                head2 = head2.next

        return dummy.next  # Return intersection list starting from dummy.next




#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = input().split()
        input2 = input().split()

        head1, tail1 = None, None
        for item in input1:
            new_node = Node(int(item))
            if not head1:
                head1 = new_node
                tail1 = new_node
            else:
                tail1.next = new_node
                tail1 = new_node

        head2, tail2 = None, None
        for item in input2:
            new_node = Node(int(item))
            if not head2:
                head2 = new_node
                tail2 = new_node
            else:
                tail2.next = new_node
                tail2 = new_node

        ob = Solution()
        result = ob.findIntersection(head1, head2)
        print_list(result)
        print("~")

# } Driver Code Ends