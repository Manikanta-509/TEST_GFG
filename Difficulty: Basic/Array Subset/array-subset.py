#User function Template for python3
class Solution:
    def isSubset(self, a, b):
        # Dictionary to store the frequency of elements in 'a'
        freq_a = {}
        for num in a:
            freq_a[num] = freq_a.get(num, 0) + 1

        # Check if each element in 'b' appears in 'a' with sufficient count
        for num in b:
            if freq_a.get(num, 0) == 0:
                return False
            freq_a[num] -= 1
        
        return True


    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends