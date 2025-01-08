

class Solution:
    def medianOf2(self, a,b):
        arr=a+b
        arr.sort()
        d=len(arr)
        if d%2==0:
            median1=arr[d//2]
            median2=arr[d//2-1]
            median3=(median1+median2)/2
            if median3.is_integer():
                return int(median3)
            else:
                return median3
                
        else:
            median=arr[d//2]
            return median
            #code here

        #code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        ob = Solution()

        if len(arr2) == 1 and arr2[0] == 0:
            arr2 = []
        ans = ob.medianOf2(arr1, arr2)
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)
        print("~")

# } Driver Code Ends