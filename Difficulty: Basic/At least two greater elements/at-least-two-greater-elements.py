#User function Template for python3

class Solution:
    def findElements(self,arr):
        if len(arr)<2:
            return -1
        a=sorted(arr)
        return a[:-2]# Your code goes here
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(*ob.findElements(arr))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends