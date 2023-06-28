class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        weights=list(map(lambda x:-math.log2(x),succProb))
        graph=defaultdict(list)
        for (u,v),w in zip(edges,weights):
            graph[u].append([v,w])
            graph[v].append([u,w])

        dist={}
        q=[(0,start)]
        while q:
            w,u=heapq.heappop(q)
            if u in dist:
                continue

            dist[u]=w
            if u==end:
                break

            for v,w in graph[u]:
                if v not in dist or dist[v]>dist[u]+w:
                    heapq.heappush(q,(dist[u]+w,v))

        return 2**(-dist[end]) if end in dist else 0.0                    