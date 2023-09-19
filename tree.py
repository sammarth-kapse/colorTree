from collections import deque

color_map = {
    'B': 'R',
    'R': 'B'
}


class TreeNode:
    def __init__(self, val=0, left=None, right=None, color='G'):
        self.val = val
        self.left = left
        self.right = right
        self.color = color


class ColorTree:

    def __init__(self, root):
        self.root = root
        self.left_boundary = []
        self.right_boundary = []
        self.leaves = []

    def traverse_tree(self):
        root = self.root
        if not root:
            return

        queue = deque([[root, 0]])
        while queue:
            length = len(queue)

            self.left_boundary.append(queue[0][0])
            if length != 1:
                self.right_boundary.append(queue[-1][0])

            for ind in range(length):
                node, width = queue.popleft()

                # Check for middle leaves; not already in left or right boundary
                if ind != 0 and ind != length-1 and not node.left and not node.right:
                    self.leaves.append([node, width])

                if node.left:
                    queue.append([node.left, width-1])
                if node.right:
                    queue.append([node.right, width+1])

    @staticmethod
    def color_outer_nodes(outer_nodes):
        current_color = 'B'
        for node in outer_nodes:
            node.color = current_color
            current_color = color_map[current_color]

    def handler(self):
        root = self. root
        if root is None:
            return
        self.traverse_tree()

        sorted_leaves = self.get_sorted_leave()
        self.right_boundary = self.right_boundary[::-1]  # Since we move in anticlockwise
        outer_nodes = self.left_boundary + sorted_leaves + self.right_boundary
        self.color_outer_nodes(outer_nodes)

    def get_sorted_leave(self):
        self.leaves.sort(key=lambda x: x[1])
        return [leave[0] for leave in self.leaves]

    def print_tree_colors_level_order(self):
        root = self.root
        if root is None:
            return

        queue = deque([root])
        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()
                print(node.color, end=' ')

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
