#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def take():
    # Reads a line of input and converts it into a list of integers
    return list(map(int, input().strip().split()))


def input_list(size, values):
    if size == 0:
        return None

    # Create the head node
    head = Node(values[0])
    tail = head

    # Create the remaining nodes
    for i in range(1, size):
        tail.next = Node(values[i])
        tail = tail.next

    return head



# } Driver Code Ends
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def intersectPoint(self, head1, head2):
        l1=head1
        l2=head2
        while l1!=l2:
            l1=l1.next if l1 else head2
            l2=l2.next if l2 else head1
        return l1
        # code here

#{ 
 # Driver Code Starts.


if __name__ == "__main__":
    T = int(input())  # Number of test cases
    for _ in range(T):
        # Read input for the three lists
        v1 = take()
        v2 = take()
        v3 = take()

        n1, n2, n3 = len(v1), len(v2), len(v3)

        # Create the linked lists
        head1 = input_list(n1, v1)
        head2 = input_list(n2, v2)
        common = input_list(n3, v3)

        # Link the common list to the end of the two lists
        temp = head1
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = common

        temp = head2
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = common

        # Find the intersection point
        solution = Solution()
        intersect_node = solution.intersectPoint(head1, head2)
        if intersect_node:
            print(intersect_node.data)
        else:
            print("No intersection")
        print("~")
# } Driver Code Ends