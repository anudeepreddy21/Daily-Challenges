class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #traverse the list
        #remember previous temp and search for next high temp/warm day
        length = len(temperatures)
        if length <=1:
            return [0]
        stck = []
        ans = [0] * length
        for cur_day in range(length-1, -1,-1): #traversing the temperatures from last index 
            # print(cur_day)
            cur_temp = temperatures[cur_day] #taking the temperature of the current index(which is from last to first here
            while stck and temperatures[stck[-1]] <= cur_temp: # ikada stack lo unna elements ni.. current_index temp tho compare chestunam, enduku ante compare chesi .. 
                # curr_temp tho kante thakuva unna stck elements ni tesesi.. danikante ekkuva unna vatine stck lo unchutha, so that aa.. high temp danini.. curr day temp danini..days difference ni answer loki store cheskovachu
                stck.pop() #ikada.. anni thakuva unna elements ni tesestunam stck lo nundi
            if stck:
                ans[cur_day] = stck[-1] - cur_day
            stck.append(cur_day)
        return ans
        
