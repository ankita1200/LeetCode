class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)>ceil(hour):
            return -1
        left = 1
        # maximum speed that will do
        right = 10**7
        print(right)
        while left < right:
            speed = (left+right) // 2
            total_hours = sum([ceil(d/speed) for d in dist[:-1]])+dist[-1]/speed
            if total_hours <= hour:
                # can journey with - speed
                right = speed
            else:
                left = speed+1
        return left
        
