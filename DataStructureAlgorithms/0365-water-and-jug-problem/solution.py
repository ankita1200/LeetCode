class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        seen = set()
        
        def dp(x_curr,y_curr):
            if (x_curr, y_curr) in seen:
                return False
            
            seen.add((x_curr,y_curr))
            if x_curr+y_curr == target:
                return True
            
            # fill x from source
            if (x_curr==0 and dp(x,y_curr)) or (y_curr==0 and dp(x_curr,y)):
                return True
            # empty x
            if (x_curr > 0 and dp(0,y_curr)) or  (y_curr>0 and dp(x_curr,0)):
                return True
            
            # empty x into y
            new_x = max(0,x_curr-y_curr)
            new_y = min(y, x_curr+y_curr)
            if dp(new_x,new_y):
                return True
            # empty y into x
            new_x = min(x,x_curr+y_curr)
            new_y = max(0,y_curr-x_curr)
            if dp(new_x,new_y):
                return True
            
            return False
        
        return dp(0,0)
