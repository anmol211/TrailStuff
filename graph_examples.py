from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
    def add_edge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        queue = []
        queue.append(s)
        self.visited.add(s)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.add(i)

    def DFS(self,s):
        self.visited.add(s)
        print(s, end=" ")
        for i in self.graph[s]:
            if i not in self.visited:
                self.DFS(i)



g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
# g.BFS(2)
g.DFS(2)