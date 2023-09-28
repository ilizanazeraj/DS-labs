import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)

# Create a logger instance
logger = logging.getLogger(__name__)


class Node:
    """Node class"""

    def __init__(self, data):
        """Initializer

        Args:
            data (sting): data to be added
        """
        self.data = data
        self.right = None
        self.left = None


def insert(node, data):
    """Inserts a node

    Args:
        node (obj): Nodes to be added
        data (string): data to be stored

    Returns:
        object: node
    """

    if node is None:
        return Node(data)
    # Traverse to the right place and insert the node
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node


def InOrder(root):
    """Print the tree in inorder

    Args:
        root: root of tree
    """
    if root:
        InOrder(root.left)
        print(root.data)
        InOrder(root.right)


def PreOrder(root):
    """Prints the tree in PreOrder

    Args:
        root : the root of the tree
    """
    if root:
        print(root.data)
        PreOrder(root.left)
        PreOrder(root.right)


def PostOrder(root):
    """Prints the list PostOrder

    Args:
        root : the root of the true
    """
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data)


def find(root, key):
    """Finds an element in the tree

    Args:
        root: root of the tree
        key (string): element to be added

    Returns:
        string: returns the element or boolean
    """
    if root is None:
        return False
    if root.data == key:
        return True
    # Check Left,right
    left = find(root.left, key)
    if left:
        return True
    right = find(root.right, key)
    return right


def findNode(root, key):
    """Finds a node in the tree

    Args:
        root : The root of the tree
        key (string): the element to be searched
    """
    if find(root, key):
        print(key, " is found in BST")
    else:
        print(key, " is not present in BST")


def findMin(root):
    """Finds the minimum element in tree

    Args:
        root : minimum element of tree
    """
    while root.left:
        root = root.left
    print("Minimum value in BST is ->", root.data)


def findMinNode(root):
    """Find the minimum Node in the tree

    Args:
        root : Root of the tree

    Returns:
        root : the minimum Node
    """
    while root.left:
        root = root.left
    return root


def findMax(root):
    """Find the maximum Node in the tree

    Args:
        root : Root of the tree

    Returns:
        root : the maximum Node
    """
    while root.right:
        root = root.right
    print("Maximum value in BST is ->", root.data)


def removeNode(root, key):
    """Remove a node from the tree

    Args:
        root: root of the tree
        key (string): element to be removed

    """
    # if Tree is Empty
    if root is None:
        return root
    # Find element to be deleted
    if key < root.data:
        root.left = removeNode(root.left, key)
    elif key > root.data:
        root.right = removeNode(root.right, key)

    else:
        # if node has one child or leaf
        if root.left is None:
            current = root.right
            root = None
            return current
        elif root.right is None:
            current = root.left
            root = None
            return current
        # if node has two children, find the successor, place it in the node, delete it
        current = findMinNode(root.right)
        root.data = current.data
        root.right = removeNode(root.right, current.data)
    return root


def merge(root1, root2):
    """Merge two trees

    Args:
        root1 (Node): first tree
        root2 (Node): second tree

    Returns:
        Node: merged tree
    """
    # Create two stacks to hold elements of tree 1 and 2
    stack1 = []
    stack2 = []
    # Current node of the each BST
    current1 = root1
    current2 = root2

    # if the tree 1 is empty than the merged tree will be the tree 2
    if not root1:
        return InOrder(root2)
    # if the tree 2 is empty than the merged tree will be the tree 1
    if not root2:
        return InOrder(root1)

    # Run the loop while there are nodes not yet printed.
    while current1 or stack1 or current2 or stack2:
        if current1 or current2:
            # Push the left most node of both trees to their corresponding stack
            if current1:
                stack1.append(current1)
                current1 = current1.left

            if current2:
                stack2.append(current2)
                current2 = current2.left

        else:
            # After we have traversed any of the trees
            # we will traverse the other tree in inorder
            if not stack1:
                while stack2:
                    current2 = stack2.pop()
                    current2.left = None
                    InOrder(current2)
                    return
            if not stack2:
                while stack1:
                    current1 = stack1.pop()
                    current1.left = None
                    InOrder(current1)
                    return

            # Compare elements
            # if the element popped from tree 1 is < element from tree 2 we pop it and push it to right subtree
            # if it is larger we push it back to its stack
            current1 = stack1.pop()
            current2 = stack2.pop()
            if current1.data < current2.data:
                print(current1.data)
                current1 = current1.right
                stack2.append(current2)
                current2 = None

            else:
                print(current2.data)
                current2 = current2.right
                stack1.append(current1)
                current1 = None
