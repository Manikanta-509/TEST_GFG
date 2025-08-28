class Solution:
    def wordBreak(self, s, dictionary):
        n = len(s)
        word_set = set(dictionary)  # for O(1) lookup
        dp = [False] * (n + 1)
        dp[0] = True  # base case

        for i in range(1, n + 1):
            for w in word_set:
                if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
                    break  # no need to check further if dp[i] is True

        return dp[n]

        # code here