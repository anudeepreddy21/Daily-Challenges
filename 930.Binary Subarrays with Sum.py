class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(x):
            if x < 0: return 0 # if goal is passed as zero, function call will be helper(-1), to avoid this
            res = 0 # To keep count of subarrays
            l, cur_sum = 0, 0
            for r in range(len(nums)):
                cur_sum += nums[r]
                while cur_sum > x:
                    cur_sum -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        return helper(goal) - helper(goal - 1)
