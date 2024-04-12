class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for ch in sentence:
            d[ch]=1
        if len(d) == 26:
            return True
        else:
            return False
        
