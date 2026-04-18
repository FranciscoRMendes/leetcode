def valid(window):
    return all(count <= 1 for count in window.values())


class Solution:

    def lengthOfLongestSubstring(self, s: str):
        left = 0
        result = 0
        window = {}

        for right in range(len(s)):
            # expand right window
            x = s[right]
            window[x] = window.get(x, 0) + 1

            # shrink window until valid
            while not valid(window):
                y = s[left]
                window[y] -= 1
                if window[y] == 0:
                    del window[y]
                left += 1

            # update answer
            result = max(result, right - left + 1)

        return result

def dfs_stack(self, grid, r, c):
    rows = len(grid)
    cols = len(grid[0])

    # stack controls DFS traversal (LIFO)
    stack = [(r, c)]
    area = 0
    while stack:

        # take the most recently added cell
        row, col = stack.pop()

        # check boundaries and skip invalid cells
        # also skip water or already visited cells
        if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                grid[row][col] == 0
        ):
            continue

        # ------------------------------
        # PROCESS NODE HERE
        # ------------------------------
        # This is where you do the work
        # depending on the problem.
        #
        # Examples:
        # - count island size
        # - collect coordinates
        # - check conditions
        # - accumulate values
        # ------------------------------
        area += 1

        # mark visited permanently so we don't revisit
        grid[row][col] = 0

        # add neighboring cells to stack for exploration
        stack.append((row + 1, col))  # down
        stack.append((row - 1, col))  # up
        stack.append((row, col + 1))  # right
        stack.append((row, col - 1))  # left

    return area


def dfs_backtrack(self, board, r, c, visited, path):

    rows = len(board)
    cols = len(board[0])

    # ---------------------------------
    # 1. CHECK INVALID STATES
    # ---------------------------------
    # stop exploring if:
    # - outside grid
    # - already visited in this path
    # - fails problem condition
    if (
        r < 0 or c < 0 or
        r >= rows or c >= cols or
        (r, c) in visited
    ):
        return

    # ---------------------------------
    # 2. PROCESS NODE (CHOOSE)
    # ---------------------------------
    # do work for this node
    # examples:
    # - add letter to path
    # - accumulate score
    # - check target condition

    path.append(board[r][c])
    visited.add((r, c))

    # ---------------------------------
    # 3. CHECK SOLUTION CONDITION
    # ---------------------------------
    # examples:
    # - path length == target
    # - word matched
    # - valid combination found

    if self.is_solution(path):
        self.results.append(path.copy())

    # ---------------------------------
    # 4. EXPLORE NEIGHBORS
    # ---------------------------------
    # typical grid directions

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dr, dc in directions:
        self.dfs_backtrack(board, r + dr, c + dc, visited, path)

    # ---------------------------------
    # 5. BACKTRACK (UNDO)
    # ---------------------------------
    # remove changes so other paths
    # can explore different choices

    path.pop()
    visited.remove((r, c))


def dfs_stack_backtrack(self, board, r, c):
    rows = len(board)
    cols = len(board[0])

    # Each stack entry stores:
    # (row, col, current path, visited set)
    stack = [(r, c, [], set())]

    results = []

    while stack:
        # pop the most recent state
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
        # Add this node to the path
        new_path = path + [board[row][col]]
        new_visited = visited | {(row, col)}

        # Check if this path is a solution
        if self.is_solution(new_path):
            results.append(new_path)

        # ------------------------------
        # 3. EXPLORE NEIGHBORS
        # ------------------------------
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            # push a new state onto the stack for exploration
            stack.append((nr, nc, new_path, new_visited))

    return results


from typing import List


class Solution:

    def dfs_stack(self, grid, r, c, backtrack=False):
        """
        Stack-based DFS template for 2D grids.

        Parameters:
        - grid: List[List[int]] or List[List[str]] representing the grid
        - r, c: starting row and column
        - backtrack: bool, whether to restore visited cells after exploration
                     (needed for problems like Word Search)
        """

        rows = len(grid)
        cols = len(grid[0])

        # Stack stores cells to explore; each entry is (row, col)
        stack = [(r, c)]

        # Problem-specific accumulator
        # Examples: area for maxAreaOfIsland, coordinates for island shape, path for Word Search
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
                    grid[row][col] == 0  # already visited or water
            ):
                continue

            # ------------------------------
            # 3. PROCESS NODE (CHOOSE)
            # ------------------------------
            result += 1  # example: increment area/count
            # You can replace this with any problem-specific logic
            # Examples:
            # - append (row, col) to island_shape
            # - append letter to current path for Word Search

            # ------------------------------
            # 4. MARK VISITED
            # ------------------------------
            temp = grid[row][col]  # save original value if backtracking
            grid[row][col] = 0  # mark visited permanently or temporarily

            # ------------------------------
            # 5. EXPLORE NEIGHBORS
            # ------------------------------
            # Push neighbors onto stack
            stack.append((row + 1, col))  # down
            stack.append((row - 1, col))  # up
            stack.append((row, col + 1))  # right
            stack.append((row, col - 1))  # left

            # ------------------------------
            # 6. OPTIONAL BACKTRACKING
            # ------------------------------
            if backtrack:
                # Restore original value so other paths can reuse this cell
                grid[row][col] = temp

        return result  # problem-specific result