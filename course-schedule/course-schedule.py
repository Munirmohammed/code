class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        visited=[0]*numCourses
        indeg=[0]*numCourses
        res=[]
        q=deque()
        for i in range(numCourses):
            for j in adj[i]:
                indeg[j]+=1
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        while q:
            u=q.popleft()
            res.append(u)
            for i in adj[u]:
                if indeg[i]!=0:
                    indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        if len(res)!=numCourses:
            return False
        return True