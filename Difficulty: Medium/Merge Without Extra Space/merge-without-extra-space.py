class Solution:
    def mergeArrays(self, a, b):
        m=len(a)
        n=len(b)
        a_ele=m-1
        b_ele=0
        if m==0:
            a.extend(b)
            return
        while b_ele<n and a_ele>=0:
            if a[a_ele]>b[b_ele]:
                a[a_ele],b[b_ele]=b[b_ele],a[a_ele]
            a_ele-=1
            b_ele+=1
        a.sort()
        b.sort()
                
        # code here