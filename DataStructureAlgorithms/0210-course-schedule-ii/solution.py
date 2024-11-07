class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = {course:0 for course in range(numCourses)}
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1
        que = deque()
        for course,indeg in indegree.items():
            if indeg==0:
                que.append(course)
        ans = []
        while que:
            curr_course = que.popleft()
            ans.append(curr_course)
            for course in graph[curr_course]:
                indegree[course] -= 1
                if indegree[course]==0:
                    que.append(course)

        return ans if len(ans)==numCourses else []
        
