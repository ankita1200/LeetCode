class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph=defaultdict(set)
        indeg=Counter({c:0 for word in words for c in word})
        n=len(words)
        for word1,word2 in zip(words,words[1:]):
            for c,d in zip(word1,word2):
                if c!=d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        indeg[d]+=1
                    break
            else:
                if len(word2)<len(word1): return ""            
        
        que = deque([node for node,indegree in indeg.items() if indegree==0])
        ans=[]
        while que:
            print(que)
            currnode=que.popleft()
            ans.append(currnode)
            print(ans)
            for neighbor in graph[currnode]:
                indeg[neighbor]-=1
                if indeg[neighbor]==0:
                    que.append(neighbor)
        if len(ans)<len(indeg):
            return ""
        return "".join(ans)
                


        
            
            
            
        
