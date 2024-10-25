class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index = 0
        stack = []

        if len(pushed) != len(popped):
            return False

        for item in pushed:
            stack.append(item)
            
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1

            

        if index == len(popped) and not stack:
            return True

        return False
