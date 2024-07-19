"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(list)
        imp={}
        for emp in employees:
            empid=emp.id
            imp[empid]=emp.importance
            graph[empid]+=emp.subordinates
        print(graph)
        print(imp)
        ans=0
        proc=[id]
        while proc:
            currempid=proc.pop()
            print(currempid)
            ans+=imp[currempid]
            for empid in graph[currempid]:
                proc.append(empid)
        return ans
        

        
        
