#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        result=''
        seen=set()
        for i in str1:
            if i not in str2:
                result+=i
                seen.add(i)
        return result
        # code here 