class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      time, freq = 0, Counter(tasks)
      maxHeap = [- cnt for cnt in freq.values()]
      que = dequeue()
      while que or maxHeap:
        time += 1
        if maxHeap:
          cnt = heapq.heappop(maxHeap) + 1
          if cnt:
            que.append([cnt, time + n])
        if que and que[0][1] == time:
          heapq.heappush(maxHeap, que.popleft()[0])
      return time
