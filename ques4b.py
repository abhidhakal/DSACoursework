# Imagine you're on a treasure hunt in an enchanted forest represented by a binary tree root. Each node in the tree has
# a value representing a magical coin. Your goal is to find the largest collection of coins that forms a magical grove.
# A magical grove is defined as a subtree where:
# Every coin's value on left subtree less than to the value of the coin directly above it (parent node).
# Every coin's value on right subtree is greater than to the value of the coin directly above it (parent node).
# Every coin in the grove needs to be binary search tree.
# Your task is to find the magical grove with the highest total value of coins.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLargestMagicalGrove(root):
    def helper(node):
        if not node:
            return True, 0, float('inf'), float('-inf')

        left_is_bst, left_sum, left_min, left_max = helper(node.left)
        right_is_bst, right_sum, right_min, right_max = helper(node.right)

        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            return True, node.val + left_sum + right_sum, min(node.val, left_min), max(node.val, right_max)
        else:
            return False, max(left_sum, right_sum), float('-inf'), float('inf')

    _, max_sum, _, _ = helper(root)
    return max_sum

# Tree Structure

#        10
#       /  \
#      5    15
#     / \     \
#    1   8     7

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)

print(findLargestMagicalGrove(root))  # Output will be the sum of the largest BST subtree
