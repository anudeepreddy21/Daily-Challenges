class Solution:
    def frequencySort(self, s: str) -> str:
      count = collections.Counter(s)
      res = []
      for letter, freq in count.most_common():
        res.append(letter * freq)
      return "".join(res)
