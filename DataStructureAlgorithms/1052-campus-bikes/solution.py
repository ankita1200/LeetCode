class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        que = []
        for bike_index,bike in enumerate(bikes):
            for worker_index,worker in enumerate(workers):
                dist = abs(bike[0]-worker[0]) + abs(bike[1]-worker[1])
                que.append((dist,worker_index,bike_index))
        heapq.heapify(que)
        ans = [-1] * len(workers)
        assigned = [False] * len(bikes)
        pair_count = 0
        while que:
            dist,worker_index,bike_index = heapq.heappop(que)
            if ans[worker_index]== -1 and not assigned[bike_index]:
                ans[worker_index] = bike_index
                assigned[bike_index] = True
                pair_count += 1
            if pair_count == len(workers):
                return ans

        return ans
