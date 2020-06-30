

# Post-order traversal

def traverse(TreeNode root):
    traverse(root.left)
    traverse(root.right)
    visit(root)
