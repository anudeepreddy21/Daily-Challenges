class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
      nums.sort() #sort cheskuntundi.. so that it keeps the track of the elements from smaller lengths to larger lengths
      prev_sum = 0 # idi previous elements sum maintain chydaniki, so that ee sum ni current element tho compare chesi, thakkuvunte ans la assign ccheskovali ledante move forward
      ans = -1
      for num in nums:
        if num < prev_sum:
          ans = num + prev_sum
        prev_sum += num
      return ans
