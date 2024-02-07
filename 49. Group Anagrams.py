class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for ch in strs:
            
            res[tuple(sorted(ch))].append(ch)
            # print(res.values())
        return res.values()




        # res = collections.defaultdict(list)

        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c)-ord('a')]+=1
        #     res[tuple(count)].append(s)
        # return res.values()
