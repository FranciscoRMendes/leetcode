from typing import List


class Solution:

    def dfs(self, grid, r, c):
        rows = len(grid)
        cols = len(grid[0])

        if r < 0 or c < 0 or r >= rows or c >= cols:
            return

        if grid[r][c] == "0":
            return

        grid[r][c] = "0"

        # explore neighbors
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)

    def dfs_stack(self, grid, r, c):

        rows = len(grid)
        cols = len(grid[0])

        # stack controls DFS traversal (LIFO)
        stack = [(r, c)]

        while stack:

            # take the most recently added cell
            row, col = stack.pop()

            # check boundaries and skip invalid cells
            # also skip water or already visited cells
            if (
                    row < 0 or col < 0 or
                    row >= rows or col >= cols or
                    grid[row][col] == "0"
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

            # mark visited permanently so we don't revisit
            grid[row][col] = "0"

            # add neighboring cells to stack for exploration
            stack.append((row + 1, col))  # down
            stack.append((row - 1, col))  # up
            stack.append((row, col + 1))  # right
            stack.append((row, col - 1))  # left



    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    self.dfs_stack(grid, r, c)

        return islands



if __name__ == '__main__':

    sol = Solution()

    # Test Case 1
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print("Test Case 1")
    print("Input:")
    for row in grid1:
        print(row)

    print("Output:", sol.numIslands(grid1))
    print("Expected: 3\n")

    # Test Case 2
    grid2 = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]

    print("Test Case 2")
    print("Input:")
    for row in grid2:
        print(row)

    print("Output:", sol.numIslands(grid2))
    print("Expected: 1")

