class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        @cache
        def assign(worker_index,available):
            if worker_index==len(workers):
                return 0
            mindist = float('inf')
            for index,bike in enumerate(bikes):
                mask = 1 << index
                if mask & available == 0:
                    d = abs(bike[0]-workers[worker_index][0]) + abs(bike[1]-workers[worker_index][1])
                    # set index to 1
                    available = available | mask
                    remdist = assign(worker_index+1,available)
                    mindist = min(mindist,d+remdist)
                    # unset the current worker index 
                    available = mask ^ available
            return mindist
        
        return assign(0,0)

