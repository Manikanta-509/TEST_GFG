#User function Template for python3

class Solution:
    def getTable(self,n):
        table=[]
        for i in range(1,11):
            a=n*i
            table.append(a)
        return table