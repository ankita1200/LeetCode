class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2*self.n)
        pos = 0
        for i in range(self.n,2*self.n):
            self.tree[i] = nums[pos]
            pos +=1
        for i in range(self.n-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
        

    def update(self, index: int, val: int) -> None:
        pos = index + self.n
        self.tree[pos] = val
        while pos > 0:
            left = right = pos
            if pos%2 == 0:
                right = pos + 1
            else:
                left = pos - 1
            self.tree[pos//2] = self.tree[left] + self.tree[right]
            pos = pos // 2    
        

    def sumRange(self, left: int, right: int) -> int:
        l = left + self.n
        r = right + self.n
        sumval = 0
        while l<=r:
            if l % 2 == 1:
                sumval += self.tree[l]
                l=l+1
            if r % 2 == 0:
                sumval += self.tree[r]
                r = r-1
            l = l //2
            r = r //2
        return sumval
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
