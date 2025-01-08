class Solution:
    def smallestSubWithSum(self, x, arr):
        n=len(arr)
        start=0
        current_sum=0
        min_len=n+1
        for i in range(n):
            current_sum+=arr[i]
            while current_sum>x:
                min_len=min(min_len,i-start+1)
                current_sum-=arr[start]
                start+=1
        return min_len if min_len!=n+1 else 0
        
                
        # Your code goes here 
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(x, a))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends