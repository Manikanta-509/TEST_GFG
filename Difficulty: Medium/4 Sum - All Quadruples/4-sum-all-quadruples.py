class Solution:
    def fourSum(self, arr, target):
        arr.sort()
        n = len(arr)
        result = []
        
        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                start = j + 1
                end = n - 1

                while start < end:
                    total_sum = arr[i] + arr[j] + arr[start] + arr[end]

                    if total_sum == target:
                        result.append([arr[i], arr[j], arr[start], arr[end]])

                        while start < end and arr[start] == arr[start + 1]:
                            start += 1
                        while start < end and arr[end] == arr[end - 1]:
                            end -= 1

                        start += 1
                        end -= 1

                    elif total_sum < target:
                        start += 1
                    else:
                        end -= 1

        return result

                
                        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.fourSum(A, D)
        ans.sort()
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print()
        if (len(ans) == 0):
            print(-1)

        print("~")

# } Driver Code Ends