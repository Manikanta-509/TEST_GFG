#User function Template for python3

def Search(arr,n,k):
    count=0
    for i in range(n):
        if arr[i]==k:
            return i
    return -1
    #code here