from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left= left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(7)
root.left.left = TreeNode(4)
root.right.right = TreeNode(6)

print(level_order_traversal(root))




