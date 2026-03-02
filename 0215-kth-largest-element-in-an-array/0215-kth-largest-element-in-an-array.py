import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        for num in nums:
            heapq.heappush(result, -num)
        res = 0
        for _ in range(k):
            res = -heapq.heappop(result)
        return res