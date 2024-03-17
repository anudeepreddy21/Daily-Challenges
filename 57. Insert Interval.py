class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      length = len(intervals)
      ans = []
      idx = 0

#case1 :  when there is no overlapping of new interval
      while idx < length and intervals[idx][1] < newInterval[0]:
        ans.append(intervals[idx])
        idx += 1
      # case 2: when they are overlapping
      while idx < length and intervals[idx][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[idx][0])
        newInterval[1] = max(newInterval[1], intervals[idx][1])
        idx += 1
      ans.append(newInterval)
      
      #case3: when interval is over
      while idx < length:
        ans.append(intervals[idx])
        idx += 1
      return ans

