class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while sticks:
            stick1 = heapq.heappop(sticks)
            if not sticks:
                return cost
            stick2 = heapq.heappop(sticks)
            cost += stick1 + stick2
            heapq.heappush(sticks, stick1+stick2)
        return cost
