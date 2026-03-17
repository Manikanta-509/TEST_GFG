class Solution:
    def getMaxOccurringChar(self, s):
        freq={}
        for num in s:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        max_char=''
        max_freq=0
        for c in freq:
            if freq[c]>max_freq:
                max_freq=freq[c]
                max_char=c
            elif freq[c]==max_freq:
                max_char=min(max_char,c)
        return max_char
        #code here