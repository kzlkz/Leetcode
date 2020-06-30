
# Pre-order traversal

def traverse(TreeNode root):

    visit(root)
    traverse(root.left)
    traverse(root.right)