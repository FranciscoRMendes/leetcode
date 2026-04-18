class Solution:

    # def dfs(self, node, destination, graph, visit):
    #
    #     if node == destination:
    #         return True
    #
    #     visit[node] = True
    #
    #     for neighbor in graph[node]:
    #         if not visit[neighbor]:
    #             if self.dfs(neighbor, destination, graph, visit):
    #                 return True
    #
    #     return False


    def dfs(self, source, destination, graph, visit):
        if source == destination:
            return True
        visit[source] = True
        for neighbor in graph[source]:
            if not visit[neighbor]:
                return self.dfs(neighbor, destination, graph, visit)

        return False

    def validPath(self, n, edges, source, destination):

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = [False] * n

        return self.dfs(source, destination, graph, visit)


if __name__ == '__main__':

    sol = Solution()

    # Test Case 1
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2

    print("Test Case 1")
    print("Input:", n, edges, source, destination)
    print("Output:", sol.validPath(n, edges, source, destination))
    print("Expected: True\n")


    # Test Case 2
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5

    print("Test Case 2")
    print("Input:", n, edges, source, destination)
    print("Output:", sol.validPath(n, edges, source, destination))
    print("Expected: False")