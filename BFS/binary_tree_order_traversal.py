from collections import deque
from typing import List, Optional
from collections import deque
from typing import List, Optional

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

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

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
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

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

def build_tree(values):
    """
    Build binary tree from level-order list
    Example: [3,9,20,None,None,15,7]
    """

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
    root1 = build_tree([3,9,20,None,None,15,7])
    expected1 = [[3],[9,20],[15,7]]
    result1 = sol.levelOrder(root1)
    assert result1 == expected1, f"Test Case 1 Failed! Got {result1}"

    # Test Case 2 (single node)
    root2 = build_tree([1])
    expected2 = [[1]]
    result2 = sol.levelOrder(root2)
    assert result2 == expected2, f"Test Case 2 Failed! Got {result2}"

    # Test Case 3 (empty tree)
    root3 = build_tree([])
    expected3 = []
    result3 = sol.levelOrder(root3)
    assert result3 == expected3, f"Test Case 3 Failed! Got {result3}"

    # Test Case 4
    root4 = build_tree([1,2,3,4,5])
    expected4 = [[1],[2,3],[4,5]]
    result4 = sol.levelOrder(root4)
    assert result4 == expected4, f"Test Case 4 Failed! Got {result4}"

    print("All BFS Level Order test cases passed!")