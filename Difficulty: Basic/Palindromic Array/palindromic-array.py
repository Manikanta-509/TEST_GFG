
def isPalinArray(arr):
    for i in arr:
        a=str(i)
        b=''.join(reversed(a))
        if a!=b:
            return False
    return True
    # Code here


    # Code here



#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if isPalinArray(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends