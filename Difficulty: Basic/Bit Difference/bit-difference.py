#User function Template for python3


    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
class Solution:
    def countBitsFlip(self, a, b):
        return bin(a ^ b).count('1') 
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        ab = [int(x) for x in input().strip().split()]
        a = ab[0]
        b = ab[1]
        ob = Solution()
        print(ob.countBitsFlip(a, b))
        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends