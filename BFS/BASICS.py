"""
- 3 things for graphs: BFS/DFS, Topological Sort, Dikjstra
- Topological sort: directed acyclic graph (DAG) only. In an edge uv, u comes before v in the traversal ordering

"""

from collections import deque

# Iterative Implementation of BFS
# FIRST create the graph (with adjList = [[] for _ in nodes] or using a dictionary)
visited = [False for _ in nodes] # or an empty array to add to
def bfs(i):
    q = deque()
    q.append((i)) # OR append((level, i))
    while q:
        x, y = q.popleft() # this pops one node at a time
        for node in neighbors:
            if valid and not visited[node]:
                visited[node] = True
                q.append(node) # OR 
        passes += 1

    """
    if we want to deal with one order at a time..
    count = 0
    while q:
        nextQ = deque()
        for node in q:
            for dep in dependencies:
                if valid and not visited[dep]: 
                    visit[dep] = True
                    nextQ.append(dep)
        count += 1
        q = nextQ
    """



def topologicalSort(graph):
    visited = [False]*numNodes  # or a set() and add to it
    resultStack = []
    for n in nodes:
        if not visited[n]
        topologicalSortRecur(n)

    def topologicalSortRecur(node):
        visited[node] = True
        for n in child:
            if not visited[n]:
                topologicalSortRecur(child)
        resultStack.insert(0, node)


# Iterative way to do topological sort by tracking indegree
def topoInterative(graph)
    resultStack = []
    adjList = [[] for n in nodes]
    indegree = [0]*numNodes
    for i, j in edges:
        adjList[i].append(j)
        indegree[j] += 1
    
    q = deque()
    for i in range(indegree):
        if indegree[i] == 0: 
            q.apend(i)

    while q:
        i = q.popleft()
        resultStack.apoend(i) # keep track of the result order of topo
        for j in adjList[i]:
            indegree[j] -= 1
            if indegree[j] == 0: 
                q.append(j)
    

