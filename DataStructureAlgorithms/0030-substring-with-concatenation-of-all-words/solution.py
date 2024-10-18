class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_frequency = {}
        ans = []
        for word in words:
            word_frequency[word] = word_frequency.get(word,0) + 1
        window_size = len(words[0])
        end = len(s)-len(words)*len(words[0])+1
        # this loop selects start indices
        for i in range(end):
            curr_frequency = {key:val for key,val in word_frequency.items()}
            #this loop forms substrings
            for j in range(0, len(words)):
                substr = s[i+j*window_size:i+j*window_size+window_size]
                if substr in curr_frequency:
                    curr_frequency[substr] -= 1
                    if curr_frequency[substr]==0:
                        del curr_frequency[substr]
                else:
                    break
            if not curr_frequency:
                ans.append(i)
        return ans


                

        
