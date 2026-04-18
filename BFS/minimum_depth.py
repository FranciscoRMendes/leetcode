from collections import deque

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        # queue will store nodes to visit
        queue = deque([root])
        # depth starts at 1 (root is level 1)
        depth = 1

        while queue:
            # Number of nodes at the current level
            level_size = len(queue)
            # This list is just for visualization/debugging
            level_nodes = []

            # Process all nodes in the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)  # nodes at this level

                # If this is a leaf node, return depth immediately
                if not node.left and not node.right:
                    print(f"Leaf found at depth {depth}, level nodes: {level_nodes}")
                    return depth

                # Add children to the queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # After processing all nodes at this level
            print(f"Completed level {depth}, nodes: {level_nodes}")
            depth += 1