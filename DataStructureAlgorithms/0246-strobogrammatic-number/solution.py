class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rule = {'0':'0', '1':'1', '6':'9', '9':'6','8':'8'}
        check = set(['2','3','4','5','7'])
        n = int(num)
        rev = ""
        for ch in num:
            if ch in check:
                return False
            rev += rule[ch]
        rev = rev[::-1]
        return num==rev
        
