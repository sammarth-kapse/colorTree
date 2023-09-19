from tree import TreeNode, ColorTree


if __name__ == '__main__':
    root = TreeNode()
    color_tree = ColorTree(root)
    color_tree.handler()
    color_tree.print_tree_colors_level_order()
