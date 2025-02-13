#User function Template for python3

class Solution:
    def findStepKeyIndex(self, arr, k, x):
        for i in range(len(arr)):  # Traverse the array
            if arr[i] == x:
                return i  # Return the index of the first occurrence
        return -1  # Return -1 if x is not found




#{ 
 # Driver Code Starts
def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1

    sol = Solution()

    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        k, x = map(int, data[index:index + 2])
        index += 2
        ans = sol.findStepKeyIndex(arr, k, x)
        results.append(ans)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends