from typing import List


class Solution:

    def dfs_stack(self, grid, r, c):

        rows = len(grid)
        cols = len(grid[0])

        # stack controls DFS traversal (LIFO)
        stack = [(r, c)]
        area= 0
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
            area+=1

            # mark visited permanently so we don't revisit
            grid[row][col] = 0

            # add neighboring cells to stack for exploration
            stack.append((row + 1, col))  # down
            stack.append((row - 1, col))  # up
            stack.append((row, col + 1))  # right
            stack.append((row, col - 1))  # left

        return area

    def dfs(self, grid, r, c):

        rows = len(grid)
        cols = len(grid[0])

        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0

        if grid[r][c] == 0:
            return 0

        grid[r][c] = 0

        return (
                1 +
                self.dfs(grid, r + 1, c) +
                self.dfs(grid, r - 1, c) +
                self.dfs(grid, r, c + 1) +
                self.dfs(grid, r, c - 1)
        )
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        cur_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cur_area = self.dfs_stack(grid, r, c)
                    max_area = max(max_area, cur_area)

        return max_area


def run_tests(solution):

    tests = [
        (
            [
                [0,0,1,0,0],
                [1,1,1,0,0],
                [0,1,0,0,1],
                [0,0,0,1,1]
            ],
            5,
            "Island with max area 5"
        ),

        (
            [
                [1,1],
                [1,1]
            ],
            4,
            "Single island"
        ),

        (
            [
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ],
            0,
            "No islands"
        ),

        (
            [
                [1,0,0,1],
                [1,0,0,1],
                [0,0,1,1]
            ],
            4,
            "Multiple islands"
        ),
    ]

    for i, (grid, expected, description) in enumerate(tests, 1):

        # IMPORTANT: copy grid so DFS mutation doesn't affect tests
        grid_copy = [row[:] for row in grid]

        result = solution.maxAreaOfIsland(grid_copy)

        print(f"\nTest {i}: {description}")
        print("Input:")
        for row in grid:
            print(row)

        print("Output  :", result)
        print("Expected:", expected)

        if result == expected:
            print("✅ PASS")
        else:
            print("❌ FAIL")


if __name__ == "__main__":

    sol = Solution()

    run_tests(sol)
