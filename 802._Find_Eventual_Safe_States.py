class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for node, neighbours in enumerate(graph):
            for neighbour in neighbours:
                adj[neighbour].append(node)
                indegree[node] += 1
            
        # print(adj)
        q = deque()
        # print(indegree)
        for node in range(len(graph)):
            # print(node)
            if indegree[node] == 0:
                q.append(node)
                
        res = []
        while q:
​
            p = q.popleft()
            res.append(p)
            # print(p)
            for neighbour in adj[p]:
                # print(neighbour)
                indegree[neighbour] -= 1
                if indegree[neighbour]  == 0:
                    q.append(neighbour)
