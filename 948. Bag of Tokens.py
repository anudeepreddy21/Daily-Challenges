class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
      tokens.sort()
      score = max_score = 0
      left, right = 0, len(tokens) - 1
      while left <= right:
        if power > tokens[i]:
          power -= tokens[i]
          left += 1
          score += 1
          max_score = max(score, max_score)
        elif score and right > left + 1:
          power += tokens[i]
          right -= 1
          score -= 1
        else:
          break
      return max_score
          
