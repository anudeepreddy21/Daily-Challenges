

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
