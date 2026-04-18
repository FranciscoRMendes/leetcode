from typing import List


class Solution:
    def dfs(self, graph, source, visited):
        visited[source] = True

        for neighbor in range(len(graph)):
            if graph[source][neighbor] == 1 and not visited[neighbor]:
                self.dfs(graph, neighbor, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        provinces = 0

        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                self.dfs(isConnected, i, visited)

        return provinces


def run_test(isConnected, expected):
    sol = Solution()
    result = sol.findCircleNum(isConnected)

    print("Input:")
    for row in isConnected:
        print(row)

    print(f"Expected: {expected}")
    print(f"Got:      {result}")

    if result == expected:
        print("✅ PASS\n")
    else:
        print("❌ FAIL\n")


if __name__ == "__main__":
    # Test case you provided
    run_test(
        isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]],
        expected=2
    )

    # Add a few more edge cases
    run_test(
        isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        expected=3
    )

    run_test(
        isConnected=[[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        expected=1
    )

    run_test(
        isConnected=[[1]],
        expected=1
    )