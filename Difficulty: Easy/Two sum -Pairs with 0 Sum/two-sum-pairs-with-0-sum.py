class Solution:
    def getPairs(self, arr):
        
        arr.sort()
        # code here
        low=0
        high=len(arr)-1
        result=[]
        while low<high:
            mid=arr[low]+arr[high]
            if mid==0:
                result.append((arr[low],arr[high]))
                low+=1
                high-=1
                while low<high and arr[low]==arr[low-1]:
                    low+=1
                while low<high and arr[high]==arr[high+1]:
                    high-=1
            elif mid<0:
                low+=1
            else:
                high-=1
        return result
            