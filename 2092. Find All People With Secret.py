class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
      secrets = set([0, firstPerson])
      time_map = {}

      for src, des, t in meetings:
        if t not in time_map:
          time_map[t] = defaultdict(list)
        time_map[t][src].append(des)
        time_map[t][des].append(src)

      def dfs(src, adj):
        if src in visit:
          return
        visit.add(src)
        secrets.add(src)
        for nei in adj[src]:
          dfs(nei, adj[src])
      for t in sorted(time_map.keys()):
        visit = set()
        for src in time_map[t]:
            if src in secrets:
              dfs(src,time_map[t])

  return list(secrets)
