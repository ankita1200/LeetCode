class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count=Counter(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in count or count[ransomNote[i]]==0:
                return False
            count[ransomNote[i]]-=1
        return True
        
