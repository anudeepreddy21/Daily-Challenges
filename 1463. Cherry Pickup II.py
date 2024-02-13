class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
      
      ROWS = len(grid) , COLS = len(grid[0])
      cache = {}
      def dfs(r, c1, c2):
        if (r, c1, c2) in cache:
          return cache[(r, c1, c2)]
        if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) > COLS - 1:
          return 0
        if r == ROWS - 1:
          return grid[r][c1] + grid [r][c2]
        for c1_cmp in [-1, 0, 1]:
          for c2_cmp in [-1, 0, 1]:
            res = max(cache, dfs(r + 1, c1 + c1_cmp, c2 + c2_cmp)
          cache[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2]
        return cache[(r, c1, c2)]
      return dfs( 0, 0, COLS -1)
