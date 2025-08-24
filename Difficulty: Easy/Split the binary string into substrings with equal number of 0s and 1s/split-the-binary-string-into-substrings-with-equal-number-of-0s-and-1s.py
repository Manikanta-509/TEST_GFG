#Back-end complete function Template for Python 3

#Back-end complete function Template for Python 3
class Solution:
    def maxSubStr(self, S):
        count0 = count1 = 0  # Count of 0s and 1s
        balanced_count = 0  # Number of balanced substrings

        for char in s:
            if char == "0":
                count0 += 1
            else:
                count1 += 1
            
            if count0 == count1:
                balanced_count += 1  # Found a balanced substring
        
        # If total 0s and 1s are not equal, splitting fully is impossible
        return balanced_count if count0 == count1 else -1

        #Write your code here



        #Write your code here

