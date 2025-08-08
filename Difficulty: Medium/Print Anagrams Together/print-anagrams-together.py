#User function Template for python3


class Solution:

    def anagrams(self, arr):
        group={}
        for i in arr:
            key=tuple(sorted(i))
            if key not in group:
                group[key]=[]
            group[key].append(i)
        return list(group.values())
