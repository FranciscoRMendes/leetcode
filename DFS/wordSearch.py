from typing import List




class Solution:

    def is_solution(self, new_path, word):
        if new_path == word:
            return True
        return False

    def dfs_stack_backtrack(self, board, r, c, word):
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
            if self.is_solution("".join(new_path), word):
                results.append(new_path)

            # ------------------------------
            # 3. EXPLORE NEIGHBORS
            # ------------------------------
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                # push a new state onto the stack for exploration
                stack.append((nr, nc, new_path, new_visited))

        return results

    def dfs(self, board, r, c, word):
        rows = len(board)
        cols = len(board[0])

        if len(word) == 0:
            return True


        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False


        if board[r][c] != word[0]:
            return False

        temp = board[r][c]
        board[r][c] = "#"


        found = (
            self.dfs(board, r + 1, c, word[1:]) or
            self.dfs(board, r - 1, c, word[1:]) or
            self.dfs(board, r, c + 1, word[1:]) or
            self.dfs(board, r, c - 1, word[1:])
        )
        board[r][c] = temp

        return found
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                    if self.dfs_stack_backtrack(board, r, c, word):
                        return True

        return False
        
        





if __name__ == "__main__":

    sol = Solution()

    # Test Case 1 (classic example)
    board1 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word1 = "ABCCED"
    expected1 = True
    result1 = sol.exist(board1, word1)
    assert result1 == expected1, f"Test Case 1 Failed! Got: {result1}"

    # Test Case 2 (word exists along border)
    board2 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word2 = "SEE"
    expected2 = True
    result2 = sol.exist(board2, word2)
    assert result2 == expected2, f"Test Case 2 Failed! Got: {result2}"

    # Test Case 3 (word does not exist)
    board3 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word3 = "ABCB"
    expected3 = False
    result3 = sol.exist(board3, word3)
    assert result3 == expected3, f"Test Case 3 Failed! Got: {result3}"

    # Test Case 4 (single letter match)
    board4 = [
        ['A']
    ]
    word4 = "A"
    expected4 = True
    result4 = sol.exist(board4, word4)
    assert result4 == expected4, f"Test Case 4 Failed! Got: {result4}"

    # Test Case 5 (single letter no match)
    board5 = [
        ['A']
    ]
    word5 = "B"
    expected5 = False
    result5 = sol.exist(board5, word5)
    assert result5 == expected5, f"Test Case 5 Failed! Got: {result5}"

    print("All Word Search test cases passed!")