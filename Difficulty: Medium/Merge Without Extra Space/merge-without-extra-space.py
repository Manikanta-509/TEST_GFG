class Solution:
    def merge(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge(left)
            self.merge(right)

            i = j = k = 0

            # Merge left and right arrays
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Copy remaining elements from left
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            # Copy remaining elements from right
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
            
    def mergeArrays(self, a, b):
        m=len(a)
        n=len(b)
        a_ele=m-1
        b_ele=0
        if m==0:
            a.extend(b)
            return
        while b_ele<n and a_ele>=0:
            if a[a_ele]>b[b_ele]:
                a[a_ele],b[b_ele]=b[b_ele],a[a_ele]
            a_ele-=1
            b_ele+=1
        self.merge(a)
        self.merge(b)

                
        # code here