
class Solution:
    def compute(self, head):
        # Step 1: Reverse the linked list
        head = self.reverseList(head)
        
        # Step 2: Remove nodes which have a greater value on left (originally right)
        max_val = head.data
        curr = head
        while curr and curr.next:
            if curr.next.data < max_val:
                curr.next = curr.next.next  # delete the node
            else:
                curr = curr.next
                max_val = curr.data
        
        # Step 3: Reverse again to restore original order
        return self.reverseList(head)

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
