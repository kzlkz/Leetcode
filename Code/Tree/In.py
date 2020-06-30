
# In-order traversal
def traverse(TreeNode root):
    traverse(root.left)
    visit(root)
    traverse(root.right)
