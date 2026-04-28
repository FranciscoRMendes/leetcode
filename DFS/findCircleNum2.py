from typing import List


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        # ------------------------------
        # 1. BUILD ADJACENCY LIST
        # ------------------------------
        graph = {i: [] for i in range(n)}
        for u in range(n):
            for v in range(n):
                if isConnected[u][v] == 1 and u != v:
                    graph[u].append(v)

        visited = set()
        components = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        # ------------------------------
        # 2. COUNT COMPONENTS
        # ------------------------------
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components


if __name__ == '__main__':
    sol = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(sol.findCircleNum(isConnected))  # Expected: 2
