
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones, zeros = 0, 0
        diff_index = {} # to keep track of diff in counts b/w 0's and 1's 
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1
            if ones - zeros not in diff_index: #to keep track of differences with index
                diff_index[ones - zeros] = i
            if ones == zeros:
                res = ones + zeros
            else:
                idx = diff_index[ones - zeros]
                res = max(res, i - idx)
        return res
