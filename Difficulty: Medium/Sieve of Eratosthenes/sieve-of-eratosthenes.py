class Solution:
    def sieve(self, n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False

        for i in range(2, n + 1):
            if prime[i]:
                for j in range(i * 2, n + 1, i):
                    prime[j] = False

        ans = []
        for i in range(2, n + 1):
            if prime[i]:
                ans.append(i)

        return ans
