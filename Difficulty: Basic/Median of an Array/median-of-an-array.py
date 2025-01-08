

class Solution:
    def findMedian(self, arr):
        arr.sort()
        d=len(arr)
        if d%2==0:
            median1=arr[d//2]
            median2=arr[d//2-1]
            median3=((median1+median2)/2)
            return median3
        else:
            median=arr[d//2]
            return (median)
        #code here.



#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Reading the number of test cases
    for _ in range(t):
        arr = list(map(int,
                       input().strip().split())
                   )  # Reading and converting input to a list of integers
        solution = Solution()
        ans = solution.findMedian(
            arr)  # Calling the function and printing the result
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends