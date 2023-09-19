# Tree Coloring Algorithm

## Introduction

This is a Python implementation of an algorithm to color a binary tree according to specific rules:
* Color Inner Nodes - Green
* Color Outer Nodes - Blue, Red in alternate fashion in anti-clockwise starting from root

### Definition
* Inner Nodes - Covered from 4 sides
* Outer Nodes -
  * Root
  * Leftmost of a level
  * Rightmost of a level
  * Leaves

## Algorithm
* **Initialization**: 
  * All nodes are Green colored in start.
  * Note root.
  * Make empty lists for leaves, left_boundary, right_boundary

* **Traverse the Tree**:
  * Use breadth-first traversal, with tracking node width.
  * Store first node of each level in left_boundary.
  * Store last node of each level in right_boundary.
  * Store middle [node, width] of each leaves in leaves
    * We store/ use width since leaves can be at any level of the tree.
    * With width, we can sort later signifying vertical position of leaf node.

* **Coloring Nodes**:
   * We make list of **outer_nodes** in following order
     * left_boundary - as it is
     * leaves - Upon Sorting based on width (vertical position of leaf node)
     * right_boundary - in reverse order for anti-clockwise traversal
   * Color OuterNodes with Blue ('B') and Red ('R') alternatively.
     * Color Switching Rule: Use a color map to switch between Blue and Red colors.
     * Note that: inner nodes were already green at initialization.

* **Print Colored Tree**:
  * After coloring, print the tree in level-order traversal.
  * Helps in visualising the result

This algorithm ensures that inner nodes of the tree are left uncolored ('G'), while the outer nodes are colored alternately in a counterclockwise manner, starting from the root.

The algorithm maintains the anticlockwise order and avoids recoloring nodes that are part of the inner tree structure.

Overall, this algorithm efficiently colors a binary tree according to the specified rules.


## Time and Space Complexity

### Time Complexity

- The time complexity of the tree traversal (breadth-first traversal) is O(n), where n is the number of nodes in the tree.
- The time complexity of sorting the leaves is O(k * log(k)), where k is the number of middle leaves. In the worst case, k can be O(n/2).
- Overall Time Complexity is O(n * log(n))

### Space Complexity

- The space complexity of the algorithm is O(n) due to the space required for the breadth-first traversal queue and other data structures.
- Overall Space Complexity is O(n)



________________

## Running the Code

To run the code, follow these steps:

1. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the code files to your local machine.
    ```
    git clone git@github.com:sammarth-kapse/colorTree.git
   ```

3. Open a terminal or command prompt and navigate to the directory containing the code files.

4. Run the `main.py` file using the following command:

    ```
   python main.py
   ```

## Test Cases

* The code includes several test cases in the `test.py` file. 
* These test cases cover various scenarios to ensure the algorithm functions correctly. 
* You can add your own test cases by extending the `TestTreeColor` class.
* test_case_additional method is a test case designed by me.

#### Logic
* Create Expected Tree.
* Create a deep-copy with same values but not color.
* Now run the color-tree algorithm on this tree.
* Assert that tree and expected trees are same

_______________