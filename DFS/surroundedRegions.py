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

        return result

    def dfs(self, board, r, c):
        rows = len(board)
        cols = len(board[0])

        if r < 1 or c < 1 or r >= rows-1 or c >= cols-1:
            return

        if board[r][c] == "X":
            return

        board[r][c] = "X"

        # explore neighbors
        self.dfs(board, r + 1, c)
        self.dfs(board, r - 1, c)
        self.dfs(board, r, c + 1)
        self.dfs(board, r, c - 1)


    def solve(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])

        # check if no X's are present in the board
        m = [l for l in board if "X" in l]
        if m == []:
            return
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    self.dfs(board, r, c)


if __name__ == "__main__":

    sol = Solution()

    # Helper to copy a board
    import copy

    # Test Case 1
    board1 = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    expected1 = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ]
    sol.solve(board1)
    assert board1 == expected1, f"Test Case 1 Failed! Got: {board1}"

    # Test Case 2 (all O's)
    board2 = [
        ["O","O","O"],
        ["O","O","O"],
        ["O","O","O"]
    ]
    expected2 = [
        ["O","O","O"],
        ["O","O","O"],
        ["O","O","O"]
    ]
    sol.solve(board2)
    assert board2 == expected2, f"Test Case 2 Failed! Got: {board2}"

    # Test Case 3 (mixed, no surrounded regions)
    board3 = [
        ["X","O","X"],
        ["O","X","O"],
        ["X","O","X"]
    ]
    expected3 = [
        ["X","O","X"],
        ["O","X","O"],
        ["X","O","X"]
    ]
    sol.solve(board3)
    assert board3 == expected3, f"Test Case 3 Failed! Got: {board3}"

    # Test Case 4 (single surrounded O)
    board4 = [
        ["X","X","X","X"],
        ["X","O","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"]
    ]
    expected4 = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"]
    ]
    sol.solve(board4)
    assert board4 == expected4, f"Test Case 4 Failed! Got: {board4}"

    print("All test cases passed!")