import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatten = [val for row in matrix for val in row]
        heapq.heapify(flatten)
        result = 0
        for _ in range(k):
            result = heapq.heappop(flatten)
        return result