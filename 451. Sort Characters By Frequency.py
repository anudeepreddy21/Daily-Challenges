class Solution:
    def frequencySort(self, s: str) -> str:
      res = collections.Counter(s)
      
      for letter, freq in res.most_common():
        res.append(letter * freq)
      return "".join(res)
