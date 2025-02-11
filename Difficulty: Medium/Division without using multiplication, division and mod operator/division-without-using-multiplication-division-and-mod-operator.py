# User function Template for python3
class Solution:
    def divide(self, dividend, divisor):


        negative = (dividend < 0) ^ (divisor < 0)  
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        temp_divisor, multiple = divisor, 1

        while (temp_divisor << 1) <= dividend:
            temp_divisor <<= 1
            multiple <<= 1

        while dividend >= divisor:
            if dividend >= temp_divisor:
                dividend -= temp_divisor
                quotient += multiple
            temp_divisor >>= 1  # Reduce divisor
            multiple >>= 1  # Reduce corresponding quotient value

        return -quotient if negative else quotient


    
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        inp = list(map(int, input().split()))

        a = inp[0]
        b = inp[1]

        ob = Solution()

        print(ob.divide(a, b))

        print("~")

# } Driver Code Ends