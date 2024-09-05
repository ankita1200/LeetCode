class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        l = len(beginWord)
        for word in wordList:
            for i in range(l):
                graph[word[:i] + "*" + word[i+1:]].append(word)
        
        que = deque([(beginWord,1)])
        visited = {beginWord : True}
        while que:
            current_word,level = que.popleft()
            for i in range(l):
                intermediate_word = current_word[:i] + "*"+current_word[i+1:]
                for word in graph[intermediate_word]:
                    if word == endWord:
                        return level+1
                    if not word in visited:
                        visited[word] = True
                        que.append((word,level+1))
                graph[intermediate_word] = []
        return 0  
        

        
