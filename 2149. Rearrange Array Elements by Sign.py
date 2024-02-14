class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length % 2 != 0:
            return []
        # eve_idx, odd_idx = 0, 1
        pos_idx, neg_idx, ans = 0, 1, [0] * length
        for num in nums:
            if num >= 0:
                ans[pos_idx] = num
                pos_idx +=2
            else:
                ans[neg_idx] = num
                neg_idx += 2
        return ans
