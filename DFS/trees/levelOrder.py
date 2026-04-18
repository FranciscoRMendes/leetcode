from typing import Optional, List
from collections import deque


# ------------------------------
# Definition for a binary tree node
# ------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------
# Your solution (leave empty)
# ------------------------------
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


# ------------------------------
# Helper: Build tree from list
# ------------------------------
def build_tree(values):
    """
    Builds a binary tree from level-order list representation.
    None represents missing nodes.
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# ------------------------------
# Helper: Run test case
# ------------------------------
def run_test(values, expected, test_name):
    root = build_tree(values)

    sol = Solution()
    result = sol.levelOrder(root)

    print(f"\n{test_name}")
    print("Input:", values)
    print("Expected:", expected)
    print("Output:", result)
    print("PASS" if result == expected else "FAIL")


# ------------------------------
# Main test runner
# ------------------------------
if __name__ == "__main__":

    tests = [
        (
            [3,9,20,None,None,15,7],
            [[3],[9,20],[15,7]],
            "Classic Example"
        ),
        (
            [1],
            [[1]],
            "Single Node"
        ),
        (
            [],
            [],
            "Empty Tree"
        ),
        (
            [1,2,3,4,5],
            [[1],[2,3],[4,5]],
            "Balanced Tree"
        ),
        (
            [1,2,None,3,None,4,None],
            [[1],[2],[3],[4]],
            "Left Skewed Tree"
        )
    ]

    for values, expected, name in tests:
        run_test(values, expected, name)