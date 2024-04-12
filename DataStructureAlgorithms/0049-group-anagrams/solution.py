class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for ana in strs:
            ans[''.join(sorted(ana))].append(ana)
        return ans.values()
