class Solution:
    from collections import Counter

    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        from collections import Counter
        freq=Counter(arr)
        arr.sort(key=lambda x:(-freq[x],x))
        return arr
        #code here
