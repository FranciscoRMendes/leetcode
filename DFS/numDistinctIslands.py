from typing import List

class Solution:

    def dfs_stack(self, grid, r, c):
        """
        DFS traversal that records a path signature
        to represent the island shape.
        """

        rows = len(grid)
        cols = len(grid[0])

        # stack stores (row, col, direction)
        stack = [(r, c, "S")]  # S = start
        path_signature = []

        while stack:

            # pop most recent cell (DFS behavior)
            row, col, direction = stack.pop()

            # ------------------------------
            # 1. BOUNDARY / VISITED CHECK
            # ------------------------------
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                grid[row][col] == 0
            ):
                continue

            # ------------------------------
            # 2. PROCESS NODE
            # ------------------------------
            # record how we arrived at this cell
            path_signature.append(direction)

            # ------------------------------
            # 3. MARK VISITED
            # ------------------------------
            grid[row][col] = 0

            # ------------------------------
            # 4. EXPLORE NEIGHBORS
            # ------------------------------
            # order matters for consistent signatures
            stack.append((row, col, "B"))      # backtrack marker
            stack.append((row, col - 1, "L"))  # left
            stack.append((row, col + 1, "R"))  # right
            stack.append((row - 1, col, "U"))  # up
            stack.append((row + 1, col, "D"))  # down

            # ------------------------------
            # 5. BACKTRACK MARKER
            # ------------------------------
            # when popped later, this records returning
            # from recursion depth
            if direction == "B":
                path_signature.append("B")

        return "".join(path_signature)


    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        # store unique island signatures
        island_shapes = set()

        # ------------------------------
        # ITERATE GRID
        # ------------------------------
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:

                    signature = self.dfs_stack(grid, r, c)
                    island_shapes.add(signature)

        return len(island_shapes)


def run_tests(solution):

    tests = [
        (
            [
                [1,1,0,0,0],
                [1,1,0,0,0],
                [0,0,0,1,1],
                [0,0,0,1,1]
            ],
            1,  # both islands same shape
            "Two identical square islands"
        ),

        (
            [
                [1,1,0,1,1],
                [1,0,0,0,0],
                [0,0,0,0,1],
                [1,1,0,1,1]
            ],
            5,
            "Multiple distinct island shapes"
        ),

        (
            [
                [1,1,0],
                [1,0,0],
                [0,0,1]
            ],
            2,
            "Two different island shapes"
        ),

        (
            [
                [1,1,0,0],
                [1,0,0,0],
                [0,0,1,1],
                [0,0,1,0]
            ],
            2,
            "Two L-shaped islands"
        ),

        (
            [
                [1,0,1],
                [0,0,0],
                [1,0,1]
            ],
            1,
            "Four single-cell islands"
        )
    ]

    for i, (grid, expected, description) in enumerate(tests, 1):

        # deep copy so your DFS marking doesn't break other tests
        grid_copy = [row[:] for row in grid]

        result = solution.numDistinctIslands(grid_copy)

        print(f"Test {i}: {description}")
        print("Expected:", expected)
        print("Got     :", result)

        if result == expected:
            print("✅ PASS\n")
        else:
            print("❌ FAIL\n")


# ------------------------------
# Example usage
# ------------------------------

if __name__ == "__main__":

    sol = Solution()  # your class

    run_tests(sol)