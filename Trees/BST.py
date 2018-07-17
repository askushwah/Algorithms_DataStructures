class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        self.parent = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Add the value in the tree
    def add (self, data):
        if self.root is None:
            self.root = Node(data)
            self.root.parent = self.root
            return
        else:
            self._add(self.root, data)

    def _add(self, cur_node, data):
        if data < cur_node.data:
            if cur_node.left_child is None:
                cur_node.left_child = Node(data)
                cur_node.left_child.parent = cur_node
                return
            else:
                self._add(cur_node.left_child, data)
        elif data > cur_node.data:
            if cur_node.right_child is None:
                cur_node.right_child = Node(data)
                cur_node.right_child.parent = cur_node
                return
            else:
                self._add(cur_node.right_child, data)

        else:
            print("The value already exist")
            return

    # Get the height of the tree
    def height(self):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            return self._height(self.root, 0)
    
    def _height(self, cur_node, h):
        if cur_node is None:
            return h
        left = self._height(cur_node.left_child, h+1)
        right = self._height(cur_node.right_child, h+1)
        return max(left, right)

    # Inorder Traversal
    def inorder_traversal(self):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            print("Inorder Traversal")
            self._inorder_traversal(self.root)

    # Private function for inorder traversal
    def _inorder_traversal(self, cur_node):
        if cur_node is None:
            return
        self._inorder_traversal(cur_node.left_child)
        print(cur_node.data, end = " ")
        self._inorder_traversal(cur_node.right_child)

    # Preorder traversal
    def preorder_traversal(self):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            print("\nPreorder Traversal")
            self._preoder_traversal(self.root)

    # Private function for preorder traversal
    def _preoder_traversal(self, cur_node):
        if cur_node is None:
            return
        print(cur_node.data, end=" ")
        self._preoder_traversal(cur_node.left_child)
        self._preoder_traversal(cur_node.right_child)
    
    # Postorder traversal
    def postorder_traversal(self):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            print("\nPostorder Traversal")
            self._postorder_traversal(self.root)
    # Private function for postorder traversal
    def _postorder_traversal(self, cur_node):
        if cur_node is None:
            return
        self._postorder_traversal(cur_node.left_child)
        self._postorder_traversal(cur_node.right_child)
        print(cur_node.data,end = " ")

    # Levelorder traversal
    def levelorder_traversal(self):
        if self.root is None:
            print("Tree is empty")
            return 
        else:
            print("\nLevelorder Traversal")
            self._levelorder_traversal(self.root)

    # Private function for levelorder traversal
    def _levelorder_traversal(self, cur_node):
        queue = []
        queue.append(cur_node)
        while len(queue) != 0:
            elem = queue.pop(0)
            if elem.left_child != None:
                queue.append(elem.left_child)
            if elem.right_child != None:
                queue.append(elem.right_child)
            print(elem.data, end = " ")
    
    # Get the node from data
    def get_node(self, data):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            return self._get_node(self.root, data)

    def _get_node(self, cur_node, data):
        if cur_node.data == data:
            return cur_node
        elif data < cur_node.data:
            return self._get_node(cur_node.left_child, data)
        else:
            return self._get_node(cur_node.right_child, data)

    # Remove the element from the tree
    def remove(self, data):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            self._remove(self.get_node(data))

    def _remove(self, cur_node):

        def findmin(cur_node):
            while cur_node.left_child != None:
                cur_node = cur_node.left_child
            return cur_node

        def no_of_children(node):
            no_of_children = 0
            if node.left_child != None:
                no_of_children += 1
            if node.right_child != None:
                no_of_children += 1
            return no_of_children

        parent_node = cur_node.parent
        no_of_children_ = no_of_children(cur_node)

        if no_of_children_ == 0:
            if parent_node.left_child == cur_node:
                parent_node.left_child = None
            else:
                parent_node.right_child = None
        
        elif no_of_children_ == 1:
            if cur_node.left_child != None:
                child_node = cur_node.left_child
            else:
                child_node = cur_node.right_child

            if parent_node.left_child == cur_node:
                parent_node.left_child = child_node
            else:
                parent_node.right_child = child_node
            child_node.parent = parent_node
        
        elif no_of_children_ == 2:
            successor_node = findmin(cur_node.right_child)
            cur_node.data = successor_node.data
            self._remove(successor_node)
    
    def mirror(self):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            self._mirror(self.root)
    
    def _mirror(self, cur_node):

        if cur_node != None:
            self._mirror(cur_node.left_child)
            self._mirror(cur_node.right_child)
            temp = cur_node.left_child
            cur_node.left_child = cur_node.right_child
            cur_node.right_child = temp
    
    def boundary(self):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            boundary_list = list()
            return self._bounday(self.root,boundary_list)

    def _bounday(self, cur_node, boundary_list):
        def left_leaf(cur_node):
            if cur_node != None:
                boundary_list.append(cur_node.data)
                if cur_node.left_child != None:
                    left_leaf(cur_node.left_child)
                elif cur_node.right_child != None:
                    left_leaf(cur_node.right_child)
        
        def right_leaf(cur_node):
            if cur_node != None:
                if cur_node.data not in boundary_list:
                    boundary_list.append(cur_node.data)
                if cur_node.right_child != None:
                    right_leaf(cur_node.right_child)
                elif cur_node.left_child != None:
                    right_leaf(cur_node.left_child)
        
        def leaf(cur_node):
            if cur_node != None:
                leaf(cur_node.left_child)
                if cur_node.left_child == None and cur_node.right_child == None:
                    if cur_node.data not in boundary_list:
                        boundary_list.append(cur_node.data)
                leaf(cur_node.right_child)

        left_leaf(cur_node)
        right_leaf(cur_node.right_child)
        leaf(cur_node)
        return boundary_list


BST = BinarySearchTree()
BST.add(6)
BST.add(4)
BST.add(5)
BST.add(2)
BST.add(9)
BST.add(90)
BST.add(8)
BST.add(3)
BST.add(1)
BST.add(10)
BST.add(7)
BST.inorder_traversal()
BST.preorder_traversal()
BST.postorder_traversal()
BST.levelorder_traversal()
print("The height is: ",BST.height())
#BST.mirror()
BST.levelorder_traversal()
print("\nBoundary are", BST.boundary())