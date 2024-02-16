class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      #Ikada concept entante, Backtracking. Backtracking enduku vadutunam? mamulga loops tho chylena ante chygalam, but optimized way vachesi idi. 
      #Backtracking use chestoo anni combinations cheyochu. So idi help avtundi.lets start!!!!
      remaining = target # to keep track of the desirable combination
      ans = []
      def helper(remaining, idx, comb):
        if remaining == 0:
          ans.append(list(comb))
          return
        elif remaining < 0:
          return
        for i in range(len(candidates)):
          comb.append(candidates[i])
          helper(remaining - candidates[i], i, comb)
          comb.pop()
      helper(remaining, 0, [])
      return ans
