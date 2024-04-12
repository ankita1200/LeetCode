class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def makeComb(curr,pos):
            if len(curr) == len(digits) and curr != "":
                ans.append(curr)
                return
            if pos >= len(digits):
                return
            digit = digits[pos]
            for alpha in dic[digit]:
                curr += alpha
                makeComb(curr,pos+1)
                curr = curr[:-1]
        
        dic = {'1':"", '2':"abc", '3':"def", '4':"ghi", '5':"jkl",
              '6':"mno", '7':"pqrs",'8':"tuv",'9':"wxyz"}
        
        ans = []
        makeComb("",0)
        return ans
        
