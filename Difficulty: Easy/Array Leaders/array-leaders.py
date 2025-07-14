class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders = []
        max_from_right = arr[-1]
        leaders.append(max_from_right)

        # Traverse from second last to the start
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders.append(arr[i])

        # Reverse the list to maintain original order of leaders
        leaders.reverse()
        return leaders

        # code here