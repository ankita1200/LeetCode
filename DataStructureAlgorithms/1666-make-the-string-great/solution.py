class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for curr in s:
            if stack and abs(ord(curr)-ord(stack[-1]))==32:
                stack.pop()
            else:
                stack.append(curr)
        return "".join(stack)
        
