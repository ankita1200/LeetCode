class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # trim the trailing spaces
        p = len(s) - 1
        while p >= 0 and s[p] == " ":
            p -= 1

        # compute the length of last word
        length = 0
        while p >= 0 and s[p] != " ":
            p -= 1
            length += 1
        return length
