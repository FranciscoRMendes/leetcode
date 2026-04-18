from typing import List


class Solution:
    def dfs_stack(self, grid, r, c, scolor, color, backtrack=False):
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
                    grid[row][col] != scolor  # already visited or water
            ):
                continue

            # ------------------------------
            # 3. PROCESS NODE (CHOOSE)
            # ------------------------------
            grid[row][col] = color
            # example: increment area/count
            # You can replace this with any problem-specific logic
            # Examples:
            # - append (row, col) to island_shape
            # - append letter to current path for Word Search

            # ------------------------------
            # 4. MARK VISITED
            # ------------------------------
            # temp = grid[row][col]  # save original value if backtracking
            # grid[row][col] = 0  # mark visited permanently or temporarily

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
            # if backtrack:
            #     Restore original value so other paths can reuse this cell
                # grid[row][col] = temp
        return result

    def dfs(self, image, r, c, scolor, color):
        rows = len(image)
        cols = len(image[0])

        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != scolor:
            return

        image[r][c] = color
        # explore neighbors
        self.dfs(image, r + 1, c, scolor, color)
        self.dfs(image, r - 1, c, scolor, color)
        self.dfs(image, r, c + 1, scolor, color)
        self.dfs(image, r, c - 1, scolor, color)

        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        scolor = image[sr][sc]
        if scolor == color:
            return image
        self.dfs_stack(image, sr, sc, scolor, color)
        return image

def run_flood_fill_tests(solution):
    """
    Test harness for the floodFill method.
    Each test case is a tuple:
    (image, sr, sc, newColor, expected_result, description)
    """
    tests = [
        (
            [
                [1, 1, 1],
                [1, 1, 0],
                [1, 0, 1]
            ],
            1, 1, 2,
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
            "Basic example with 2D connected region"
        ),
        (
            [
                [0, 0, 0],
                [0, 1, 1]
            ],
            1, 1, 1,
            [[0, 0, 0], [0, 1, 1]],
            "Single pixel change (new color same as original)"
        ),
        (
            [
                [0, 0, 0],
                [0, 0, 0]
            ],
            0, 0, 2,
            [[2, 2, 2], [2, 2, 2]],
            "Entire image recolor"
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            0, 0, 5,
            [[5, 2, 3], [4, 5, 6], [7, 8, 9]],
            "No connected region except starting cell"
        )
    ]

    for i, (image, sr, sc, newColor, expected, desc) in enumerate(tests, 1):
        # deep copy the image so original test data is preserved
        import copy
        image_copy = copy.deepcopy(image)

        result = solution.floodFill(image_copy, sr, sc, newColor)

        print(f"Test {i}: {desc}")
        print("Input image:")
        for row in image:
            print(row)
        print("Start:", (sr, sc), "New Color:", newColor)
        print("Output:")
        for row in result:
            print(row)
        print("Expected:")
        for row in expected:
            print(row)
        print("✅ PASS\n" if result == expected else "❌ FAIL\n")


# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    sol = Solution()
    run_flood_fill_tests(sol)