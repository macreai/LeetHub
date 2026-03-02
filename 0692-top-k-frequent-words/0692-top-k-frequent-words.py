import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)

        heap = []
        for word, count in counts.items():
            heapq.heappush(heap, (-count, word))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result