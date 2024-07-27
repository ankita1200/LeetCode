class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return
        free_rooms=[]
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(free_rooms,intervals[0][1])
        for start,end in intervals[1:]:
            if start>=free_rooms[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms,end)
        return len(free_rooms)
        
