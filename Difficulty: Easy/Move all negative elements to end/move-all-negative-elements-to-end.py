#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        a=[]
        b=[]
        for i in range(len(arr)):
            if arr[i]>=0:
                a.append(arr[i])
            else:
                b.append(arr[i])
        arr[:]=a+b
        #; Your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.segregateElements(a)
        print(*a)

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends