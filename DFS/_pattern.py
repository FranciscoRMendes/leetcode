from typing import List


# -------------------------------------------------------
# DFS ON EDGE LIST (e.g. count connected components)
# -------------------------------------------------------
#
# Input:  n nodes (0..n-1), edges as pairs [u, v]
# Pattern:
#   1. Build adjacency list from edge list
#   2. Run DFS from every unvisited node
#   3. Each DFS call = one connected component
#
def dfs_edge_list(n: int, edges: List[List[int]]) -> int:

    # ------------------------------
    # 1. BUILD ADJACENCY LIST
    # ------------------------------
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected

    visited = set()
    components = 0

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    # ------------------------------
    # 2. VISIT EVERY NODE
    # ------------------------------
    for node in range(n):
        if node not in visited:
            # ------------------------------
            # 3. NEW COMPONENT FOUND
            # ------------------------------
            components += 1
            dfs(node)

    return components


class Solution:

    def dfs_stack(self, grid, r, c):

        rows = len(grid)
        cols = len(grid[0])

        stack = [(r, c)]
        result = 0

        while stack:

            # ------------------------------
            # 1. POP THE MOST RECENT CELL
            # ------------------------------
            row, col = stack.pop()

            # ------------------------------
            # 2. BOUNDARY + VISITED CHECK
            # ------------------------------
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                grid[row][col] == 0
            ):
                continue

            # ------------------------------
            # 3. PROCESS NODE (CHOOSE)
            # ------------------------------
            result += 1

            # ------------------------------
            # 4. MARK VISITED
            # ------------------------------
            grid[row][col] = 0

            # ------------------------------
            # 5. EXPLORE NEIGHBORS
            # ------------------------------
            stack.append((row + 1, col))  # down
            stack.append((row - 1, col))  # up
            stack.append((row, col + 1))  # right
            stack.append((row, col - 1))  # left

        return result

    def dfs_backtrack(self, board, r, c, visited, path):

        rows = len(board)
        cols = len(board[0])

        # ---------------------------------
        # 1. CHECK INVALID STATES
        # ---------------------------------
        if (
            r < 0 or c < 0 or
            r >= rows or c >= cols or
            (r, c) in visited
        ):
            return

        # ---------------------------------
        # 2. PROCESS NODE (CHOOSE)
        # ---------------------------------
        path.append(board[r][c])
        visited.add((r, c))

        # ---------------------------------
        # 3. CHECK SOLUTION CONDITION
        # ---------------------------------
        if self.is_solution(path):
            self.results.append(path.copy())

        # ---------------------------------
        # 4. EXPLORE NEIGHBORS
        # ---------------------------------
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            self.dfs_backtrack(board, r + dr, c + dc, visited, path)

        # ---------------------------------
        # 5. BACKTRACK (UNDO)
        # ---------------------------------
        path.pop()
        visited.remove((r, c))

    def dfs_stack_backtrack(self, board, r, c):

        rows = len(board)
        cols = len(board[0])

        # each stack entry: (row, col, current path, visited set)
        stack = [(r, c, [], set())]
        results = []

        while stack:

            row, col, path, visited = stack.pop()

            # ------------------------------
            # 1. BOUNDARY + VISITED CHECK
            # ------------------------------
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                (row, col) in visited
            ):
                continue

            # ------------------------------
            # 2. PROCESS NODE (CHOOSE)
            # ------------------------------
            new_path = path + [board[row][col]]
            new_visited = visited | {(row, col)}

            # ------------------------------
            # 3. CHECK SOLUTION CONDITION
            # ------------------------------
            if self.is_solution(new_path):
                results.append(new_path)

            # ------------------------------
            # 4. EXPLORE NEIGHBORS
            # ------------------------------
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                stack.append((row + dr, col + dc, new_path, new_visited))

        return results
