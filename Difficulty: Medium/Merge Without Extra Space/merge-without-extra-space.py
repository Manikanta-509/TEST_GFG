class Solution:
    def mergeArrays(self, a, b):
        m = len(a)
        n = len(b)
        a_ele = m - 1
        b_ele = 0
        if m==0:
            a.extend(b)
            return

        while b_ele < n and a_ele >= 0:
            if a[a_ele] > b[b_ele]:
                a[a_ele], b[b_ele] = b[b_ele], a[a_ele]
            a_ele -= 1
            b_ele += 1
        a.sort()
        b.sort()
        
       
        
            
        # code here


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

        print("~")

# } Driver Code Ends