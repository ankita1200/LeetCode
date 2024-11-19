class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        indexOnLeft = [-1]*n
        indexOnRight = [n] * n
        stack = []
        for i in range(n):
            while len(stack)>0 and heights[stack[-1]]>heights[i]:
                curr_index = stack.pop()
                indexOnRight[curr_index]=i
            stack.append(i)
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack)>0 and heights[stack[-1]]>heights[i]:
                curr_index = stack.pop()
                indexOnLeft[curr_index]=i
            stack.append(i)
        fin = [0]*n
        for i in range(n):
            fin[i]=(indexOnRight[i]-indexOnLeft[i]-1)*heights[i]
        return max(fin)

        
