from collections import deque
from typing import Optional, List


# ─── TREE BFS (level order) ───────────────────────────────────────────────────

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_tree(root: Optional[TreeNode]):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# ─── GRAPH BFS (shortest path / level distance) ───────────────────────────────

def bfs_graph(graph: dict, start, target):
    visited = {start}
    queue = deque([(start, 0)])         # (node, distance)

    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1                           # target not reachable


# ─── GRID BFS ─────────────────────────────────────────────────────────────────

def bfs_grid(grid: List[List[int]], start_r: int, start_c: int):
    rows, cols = len(grid), len(grid[0])
    visited = {(start_r, start_c)}
    queue = deque([(start_r, start_c, 0)])  # (row, col, distance)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c, dist = queue.popleft()

        # ── process node here ──────────────────────────────────────────────────

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
