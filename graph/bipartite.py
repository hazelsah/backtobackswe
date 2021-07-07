class Solution:
    def isBipartite(self, adjList):
        '''
        :type adjList: list of list of int
        :rtype: bool
        '''
        queue = []
        seen = []
        sol = []

        queue.append((0, 'red'))
        seen.append(0)
        while len(queue) > 0:
            node = queue.pop(0)
            sol.append(node)
            for item in adjList[node[0]]:
                if item not in seen:
                    if node[1] == 'red':
                        queue.append((item, 'blue'))
                        seen.append(item)
                    elif node[1] == 'blue':
                        queue.append((item, 'red'))
                        seen.append(item)
        if len(sol) != len(adjList):
            return True
        return False


# last one won't be added so length of solution will be different
if __name__ == '__main__':
    graph = [[3], [3], [4], [], []]
    s = Solution()
    print(s.isBipartite(graph))
