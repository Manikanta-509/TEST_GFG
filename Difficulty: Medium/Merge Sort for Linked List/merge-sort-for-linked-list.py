

class Solution:
    def mergeSort(self, head):
        # Base case: 0 or 1 node
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into halves
        mid = self.getMiddle(head)
        next_to_mid = mid.next
        mid.next = None  # Break the list

        # Step 2: Sort the two halves
        left = self.mergeSort(head)
        right = self.mergeSort(next_to_mid)

        # Step 3: Merge the sorted halves
        sorted_list = self.sortedMerge(left, right)
        return sorted_list

    # Helper to find middle using slow and fast pointer
    def getMiddle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Helper to merge two sorted lists
    def sortedMerge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)

        return result

        # code here