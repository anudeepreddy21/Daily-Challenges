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

# Ikkada ee problem chudagane intuition vachesi,, 2 pointer sliding window laga vadi subarrays sum chustoo count chydam subarrays ni. but ila chesthe O(n**2) ** padtundi.
# so clever way of solving thios problem is... Nenu  okate loop laga vadi first I will find out the result for <= goal. Deeni valla manaki exact goal ki kavalsina subarrays summation count radu.. but kindavi anni vastayi.
# => So manaki vahina ipudu <= goal subarray count , manaki kavalsindi == goal subarray count
# => idi solve chydaniki nenu malli <= goal - 1 subarray count techkunta.
# => Now we have subarray count for <= goal and sb. count for <= goal -1.
# => Count (res == goal) can be scieved by. doing --> count(<= goal) - Count( <= goal - 1)
