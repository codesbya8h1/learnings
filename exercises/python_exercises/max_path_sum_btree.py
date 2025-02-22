# Maximum Sum of a Continuous Path in a Binary Tree
# Hard
# Return the maximum sum of a continuous path in a binary tree. A path is defined by the following characteristics:

# Consists of a sequence of nodes that can begin and end at any node in the tree
# Each consecutive pair of nodes in the sequence is connected by an edge
# The path must be a single continuous sequence of nodes that doesn't split into multiple paths
# Example:


# Output: 30
# Constraints:
# The tree contains at least one node.


# Explain
    # 1. We need to find the maximum sum of a continuous path in a binary tree.
    # 2. We can start and end at any node in the tree.
    # 3. The path must be a single continuous sequence of nodes that doesn't split into multiple paths.
    # 4. We can use a dfs to find the maximum sum of a continuous path in a binary tree.
    # 5. We can use a nonlocal variable to store the maximum sum of a continuous path in a binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        if not node:
            return float('-inf')
        
        # Calculate the maximum sum ending at the current node
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        
        # The maximum sum ending at this node
        max_ending_here = max(node.val, node.val + max(left_sum, right_sum))
        
        # Update the global maximum if necessary
        max_sum = max(max_sum, max_ending_here, node.val + left_sum + right_sum)
        
        return max_ending_here
    
    dfs(root)
    return max_sum

# Helper function to create the tree from the given list
def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Create the tree and find the maximum path sum
values = [5,-10,8,1,-7,9,7,11,None,-1,None,None,None,6,-3]
root = create_tree(values)
result = maxPathSum(root)
print(f"The maximum sum of a continuous path is: {result}")
