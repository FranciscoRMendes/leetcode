from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:

            level_size = len(queue)

            for i in range(level_size):

                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result


def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1

    return root


if __name__ == "__main__":

    sol = Solution()

    # Test Case 1 (classic example)
    root1 = build_tree([1, 2, 3, None, 5, None, 4])
    expected1 = [1, 3, 4]
    result1 = sol.rightSideView(root1)
    assert result1 == expected1, f"Test Case 1 Failed! Got {result1}"

    # Test Case 2 (single node)
    root2 = build_tree([1])
    expected2 = [1]
    result2 = sol.rightSideView(root2)
    assert result2 == expected2, f"Test Case 2 Failed! Got {result2}"

    # Test Case 3 (empty tree)
    root3 = build_tree([])
    expected3 = []
    result3 = sol.rightSideView(root3)
    assert result3 == expected3, f"Test Case 3 Failed! Got {result3}"

    # Test Case 4 (left-skewed, rightmost is always the only node)
    root4 = build_tree([1, 2, None, 3])
    expected4 = [1, 2, 3]
    result4 = sol.rightSideView(root4)
    assert result4 == expected4, f"Test Case 4 Failed! Got {result4}"

    print("All Right Side View test cases passed!")
