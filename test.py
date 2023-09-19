from tree import TreeNode, ColorTree


class TestTreeColor(object):

    def test_case1(self):
        root = TreeNode(1, color='B')
        self.verify_test_case(root)

    def test_case2(self):
        root = TreeNode(1, color='B')
        root.left = TreeNode(2, color='R', left=TreeNode(val=4, color='B'))
        root.right = TreeNode(3, color='R', left=TreeNode(val=5, color='R'), right=TreeNode(val=6, color='B'))

        self.verify_test_case(root)

    def test_case3(self):
        root = TreeNode(1, color='B')
        root.left = TreeNode(2, color='R', left=TreeNode(val=4, color='B'))
        root.right = TreeNode(3, color='R', left=TreeNode(val=5, color='R'), right=TreeNode(val=6, color='B'))

        self.verify_test_case(root)

    def test_case4(self):
        root = TreeNode(1, color='B')
        root.left = TreeNode(2, color='R', left=TreeNode(val=4, color='B'))
        root.right = TreeNode(3, color='B', right=TreeNode(val=6, color='R'))

        self.verify_test_case(root)

    def test_case5(self):
        left_sub = TreeNode(2, color='R')
        left_sub.left = TreeNode(4, color='B', left=TreeNode(val=8, color='R'))
        left_sub.right = TreeNode(5, color='G', left=TreeNode(val=9, color='B'))

        right_sub = TreeNode(3, color='R', left=TreeNode(6, color='R'))
        right_sub.right = TreeNode(7, color='B', left=TreeNode(val=10, color='B'), right=TreeNode(val=11, color='R'))

        root = TreeNode(1, color='B', left=left_sub, right=right_sub)

        self.verify_test_case(root)

    def test_case_additional(self):
        left_sub = TreeNode(2, color='R')
        left_sub.left = TreeNode(4, color='B', left=TreeNode(val=8, color='R'))
        left_sub.right = TreeNode(5, color='G', left=TreeNode(val=9, color='B'))

        right_sub = TreeNode(3, color='R')
        right_sub.left = TreeNode(6, color='G', left=TreeNode(val=12, color='R'))
        right_sub.right = TreeNode(7, color='B', left=TreeNode(val=10, color='B'), right=TreeNode(val=11, color='R'))

        root = TreeNode(1, color='B', left=left_sub, right=right_sub)

        self.verify_test_case(root)

    def verify_test_case(self, expected_tree):
        tree = self.copy_tree_without_color(expected_tree)
        color = ColorTree(tree)
        color.handler()

        self.assert_trees(tree, expected_tree)

    def copy_tree_without_color(self, tree):
        if tree is None:
            return None

        # Only copying Val
        new_node = TreeNode(val=tree.val)

        new_node.left = self.copy_tree_without_color(tree.left)
        new_node.right = self.copy_tree_without_color(tree.right)

        return new_node

    def assert_trees(self, node, expected_node):
        if not node and not expected_node:
            return
        if not node or not expected_node:
            assert False
        self.assert_trees(node.left, expected_node.left)
        self.assert_trees(node.right, expected_node.right)
        assert node.val == expected_node.val and node.color == expected_node.color
