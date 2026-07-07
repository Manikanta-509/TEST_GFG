class Solution:
    def countArray(self, arr, x):
        result=[]
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in arr:
            avg=(i+x)//2
            if avg in freq:
                result.append(freq[avg])
            else:
                result.append(0)
        return result
        # code here
        