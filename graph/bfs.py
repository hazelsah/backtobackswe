from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, vs):
        for v in vs:
            self.graph[u].append(v)

    def print_graph(self):
        for v in self.graph:
            print(v, self.graph[v])

    def bfs(self, u):
        q = []
        seen = []
        sol = []
        q.append(u)
        seen.append(u)
        while len(q) > 0:
            node = q.pop(0)
            sol.append(node)
            for t in self.graph[node]:
                if t not in seen:
                    q.append(t)
                    seen.append(t)

        print('sol', sol)


if __name__ == '__main__':
    g = Graph()
    g.addEdge('A', ['B', 'J', 'G'])
    g.addEdge('B', ['A', 'D'])
    g.addEdge('D', ['B', 'J', 'H'])
    g.addEdge('J', ['D', 'A', 'G'])
    g.addEdge('G', ['A', 'F', 'E', 'J'])
    g.addEdge('F', ['H', 'I', 'G', 'E'])

    g.print_graph()
    g.bfs('A')
