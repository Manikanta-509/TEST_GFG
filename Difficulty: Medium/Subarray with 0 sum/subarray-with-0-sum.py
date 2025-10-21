#User function Template for python3

class Solution:
    def subArrayExists(self, arr):
        sum_index_map = {}
        current_sum = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            if current_sum == 0 or current_sum in sum_index_map:
                return True
            sum_index_map[current_sum] = i
        return False
  #Return true or false


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        if (Solution().subArrayExists(arr)):
            print("true")
        else:
            print("false")

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends