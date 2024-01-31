class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #traverse the list
        #remember previous temp and search for next high temp/warm day
        length = len(temperatures)
        if length <=1:
            return [0]
        stck = []
        ans = [0] * length
        for cur_day in range(length-1, -1,-1):
            print(cur_day)
            cur_temp = temperatures[cur_day]
            while stck and temperatures[stck[-1]] <= cur_temp:
                stck.pop()
            if stck:
                ans[cur_day] = stck[-1] - cur_day
            stck.append(cur_day)
        return ans
