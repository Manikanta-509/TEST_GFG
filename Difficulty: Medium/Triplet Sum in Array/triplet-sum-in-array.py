
class Solution:
     
    # Should return true if there exists a triplet in the
    # array arr[] which sums to x. Otherwise false
    def hasTripletSum(self, arr, target):
        n=len(arr)
        arr.sort()
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                current_value=arr[i]+arr[left]+arr[right]
                if current_value==target:
                    return 1
                elif current_value<target:
                    left+=1
                else:
                    right-=1
        return 0
            
        # Your Code Here

        # Your Code Here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array
        target = int(input().strip())  # Read the target sum
        ob = Solution()
        print("true"
              if ob.hasTripletSum(arr, target) else "false")  # Output result
        tc -= 1

# } Driver Code Ends