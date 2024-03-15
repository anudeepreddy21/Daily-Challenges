class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      length = len(nums)
      ans = [1] * length
      for L in range(length):
        ans[L] = ans[L - 1] * nums[L - 1]
      R = 1
      for i in range(length - 1, -1, -1):
        ans[i] = ans[i] * R
        R = R * nums[i]
      return ans
