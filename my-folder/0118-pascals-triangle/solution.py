class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        pascal.append([1])
        if numRows == 1:
            return pascal
        pascal.append([1,1])
        
        for i in range(3, numRows+1):
            prevrow = pascal[-1]
            f = []
            f.append(prevrow[0])
            for j in range(len(prevrow)-1):
                f.append(prevrow[j]+prevrow[j+1])
            f.append(prevrow[-1])
            pascal.append(f)
        return pascal
