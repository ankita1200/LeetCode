class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        cnt={x:0 for x in range(numCourses)}
        indeg={x:[] for x in range(numCourses)}
        for u,v in prerequisites:
            indeg[v].append(u)
            cnt[u]+=1
        
        que=deque()
        for key,val in cnt.items():
            if val==0:
                que.append(key)
        tp=[]
        while que:
            node=que.popleft()
            if node in tp:
                return []
            tp.append(node)
            for course in indeg[node]:
                cnt[course]-=1
                if cnt[course]==0:
                    que.append(course)
            
        return tp if len(tp)==numCourses else []
    

        
        
        
