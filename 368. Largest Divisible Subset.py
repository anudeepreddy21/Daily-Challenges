class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # """
        # :type nums: List[int]
        # :rtype: List[int]
        # """
        # if len(nums) == 0:
        #     return []

        # # important step !
        # nums.sort()
        
        # # The container that keep the size of the largest divisible subset that ends with X_i
        # # dp[i] corresponds to len(EDS(X_i))
        # dp = [0] * (len(nums))
        
        # """ Build the dynamic programming matrix/vector """
        # for i, num in enumerate(nums):
        #     maxSubsetSize = 0
        #     for k in range(0, i):
        #         if nums[i] % nums[k] == 0:
        #             maxSubsetSize = max(maxSubsetSize, dp[k])

        #     maxSubsetSize += 1
        #     dp[i] = maxSubsetSize
        
        # """ Find both the size of largest divisible set and its index """ 
        # maxSize, maxSizeIndex = max([(v, i) for i, v in enumerate(dp)])
        # ret = []
        
        # """ Reconstruct the largest divisible subset """ 
        # # currSize: the size of the current subset
        # # currTail: the last element in the current subset
        # currSize, currTail = maxSize, nums[maxSizeIndex]
        # for i in range(maxSizeIndex, -1, -1):
        #     if currSize == dp[i] and currTail % nums[i] == 0:
        #         ret.append(nums[i])
        #         currSize -= 1
        #         currTail = nums[i]
        
        # return reversed(ret)
        hashmap = {}
        nums.sort()
        for i in range(len(nums)):
            temp = []
            for k,v in hashmap.items():
                if nums[i] % k == 0 and len(temp) < len(v):
                    temp = list(v)
                    # print("temp", j,temp)
            temp.append(nums[i])
            print(i,"tmp",temp,nums[i])
            hashmap[nums[i]] = list(temp)
        
        maxlist, maxlength = [], 0
        for k, v in hashmap.items():
            
            if len(maxlist) < len(v):
               
                maxlist = list(v)
        return list(maxlist)
        
