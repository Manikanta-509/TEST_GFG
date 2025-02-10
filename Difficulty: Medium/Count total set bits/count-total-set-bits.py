class Solution:
    # Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self, n):
        total = 0
        while n > 0:
            x = 0
            while (1 << x) <= n:
                x += 1
            x -= 1  # Highest power of 2 ≤ n
            
            if x == 0:  # Avoid negative shift
                bits_up_to_2x = 0
            else:
                bits_up_to_2x = x * (1 << (x - 1))

            msb_2x_to_n = n - (1 << x) + 1

            total += bits_up_to_2x + msb_2x_to_n

            n -= (1 << x)
        
        return total





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
        print("~")
# } Driver Code Ends