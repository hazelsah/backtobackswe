from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, vs):
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

    def dfs(self, u):
        q = []
        seen = []
        sol = []
        q.append(u)
        seen.append(u)
        while len(q) > 0:
            node = q.pop()
            sol.append(node)
            for t in self.graph[node]:
                if t not in seen:
                    q.append(t)
                    seen.append(t)
        print('sol', sol)

if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', ['B', 'J', 'G'])
    g.add_edge('B', ['A', 'D'])
    g.add_edge('D', ['B', 'J', 'H'])
    g.add_edge('J', ['D', 'A', 'G'])
    g.add_edge('G', ['A', 'F', 'E', 'J'])
    g.add_edge('F', ['H', 'I', 'G', 'E'])

    g.print_graph()
    g.bfs('A')
    g.dfs('A')
