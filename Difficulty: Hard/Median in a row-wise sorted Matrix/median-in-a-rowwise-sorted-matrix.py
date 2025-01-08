#User function Template for python3

class Solution:
    def median(self, mat):
        flat=[]
        R=len(mat)
        C=len(mat[0])
        for i in range(R):
            for j in range(C):
                flat.append(mat[i][j])
        flat.sort()
        d=len(flat)
        if d%2==0:
            first=flat[d//2]
            second=flat[d//2-1]
            third=(first+second)/2
            return third
        else:
            median=flat[d//2]
            return median
    	#code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        r = int(input())
        c = int(input())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t = [int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j] = t[j]
        ans = ob.median(matrix)
        print(ans)
        print("~")

# } Driver Code Ends