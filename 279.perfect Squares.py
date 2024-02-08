class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], dp[target - square] + 1)
        return dp[n]

# TLE :
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # squres = [i*i for i in range(1, n//2 + 1) if i * i <= n]
        # ans = float('inf')
        
        # def helper(remaining, idx, count):
        #     nonlocal ans
        #     if remaining == 0:
        #         ans = min(ans, count)
        #         return
        #     if remaining < 0:
        #         return
        #     for i in range(idx, len(squres)):
        #         count += 1
        #         helper(remaining - squres[i], idx, count)
        #         count -= 1
        # helper(n, 0, 0)
        # return ans
