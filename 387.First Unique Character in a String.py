class Solution:
    def firstUniqChar(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return -1
        elif length == 1:
            return 0
        dic = {}
        for i in range(length):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        for idx, ch in enumerate(s):
            if dic[ch] == 1:
                return idx
        return -1
